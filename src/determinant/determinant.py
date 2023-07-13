# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-28 10:39:02
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-13 16:44:13
from data_structures.data_structures import Payload
from fuzzywuzzy import fuzz
import helpers
from .match import match_isbn, match_title, match_author, match_publication
from typing import List


def determinant(query_data: Payload, api_response) -> bool:
    """
    Determines whether a single title from response is identical
    to input title.

    query_data: Payload
    api_response: an item in mods
    """
    input_isbn = query_data.ISBN
    input_title_jpn = query_data.FULL_TITLE
    input_author_jpn = query_data.AUTHOR
    input_publisher_jpn = query_data.PUBLISHER
    input_pub_year = query_data.PUB_YEAR

    # TODO: change data structure such that you only pass api_response once
    response_titles = helpers.get_response_titles(api_response)
    response_isbn = helpers.get_response_isbn(api_response)
    response_author_names = helpers.get_response_author_names(api_response)
    response_publish_info = helpers.get_response_publish_info(api_response)

    isbn_determinant = match_isbn(input_isbn, response_isbn)
    title_determinant = (
        match_title(input_title_jpn, response_titles)
        and match_author(input_author_jpn, response_author_names)
        and match_publication(
            input_publisher_jpn, input_pub_year, response_publish_info
        )
    )
    return isbn_determinant or title_determinant


def held_at_harvard(api_response) -> dict:
    permanent = [
        "Widener Library, Harvard University",
        "Harvard-Yenching Library, Harvard University",
    ]
    output = {"item_location": None, "permalink": None}
    if "location" in api_response:
        item_location = api_response["location"]
        if item_location and (isinstance(item_location, List)):
            if item_location[0] and "physicalLocation" in item_location[0]:
                item_location = item_location[0]["physicalLocation"]["#text"]
                if item_location in permanent:
                    output["item_location"] = item_location

    if "relatedItem" in api_response:
        relatedItem = api_response["relatedItem"]
        if not isinstance(relatedItem, List):
            relatedItem = [relatedItem]
        for item in relatedItem:
            if (
                "@otherType" in item
                and item["@otherType"] == "HOLLIS record"
                and "location" in item
            ):
                if "url" in item["location"] and item["location"]["url"]:
                    output["permalink"] = item["location"]["url"]
    return output
