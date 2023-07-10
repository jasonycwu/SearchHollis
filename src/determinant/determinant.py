# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-28 10:39:02
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-10 08:11:25
from data_structures.data_structures import Payload
from fuzzywuzzy import fuzz
import helpers
from .match import match_isbn, match_title, match_author, match_publication


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
    return match_isbn(input_isbn, response_isbn) or title_determinant

    if isbn_determinant and title_determinant:
        # print("determinant TRUE-ISBN and TITLE")
        return True
    elif isbn_determinant and not title_determinant:
        # print("determinant TRUE-ISBN only")
        return True
    elif title_determinant and not isbn_determinant:
        # print("determinant TRUE-TITLE only")
        return True
    else:
        # print("determinant FALSE")
        return False


def held_at_harvard(api_response) -> str:
    permanent = [
        "Widener Library, Harvard University",
        "Harvard-Yenching Library, Harvard University",
    ]
    if "location" in api_response:
        item_location = api_response["location"]
        # print(item_location)
        if item_location and (isinstance(item_location, list)):
            if "physicalLocation" in item_location[0]:
                item_location = item_location[0]["physicalLocation"]["#text"]
                if item_location in permanent:
                    return item_location
    return ""
