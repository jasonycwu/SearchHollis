# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-28 10:39:02
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-04 12:03:58
from data_structures.data_structures import Payload
from fuzzywuzzy import fuzz
import helpers
from .match import match_isbn, match_title


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

    if "titleInfo" in api_response:
        response_titles = helpers.get_titles_list(api_response["titleInfo"])

    if "identifier" in api_response:
        response_isbn = helpers.get_isbn_list(api_response["identifier"])

    if "name" in api_response:
        response_author_names = helpers.get_author_names_list(api_response["name"])

    # response_publisher_eng = api_response["originInfo"][0]["publisher"]
    # response_publisher_jpn = api_response["originInfo"][1]["publisher"]
    # response_pub_year = api_response["originInfo"][0]["dateIssued"]
    # response_where = api_response["location"][0]

    # print(response_titles)
    return match_isbn(input_isbn, response_isbn) or match_title(
        input_title_jpn, response_titles
    )


def held_at_harvard(api_response) -> str:
    permanent = [
        "Widener Library, Harvard University",
        "Harvard-Yenching Library, Harvard University",
    ]
    # print(api_response)
    if "location" in api_response:
        item_location = api_response["location"]
        # print(item_location)
        if type(item_location) == dict:
            item_location = [item_location]
        if "physicalLocation" in item_location[0]:
            item_location = item_location[0]["physicalLocation"]["#text"]
            # print(item_location)
            if item_location in permanent:
                return item_location
            else:
                return ""
    else:
        return ""
