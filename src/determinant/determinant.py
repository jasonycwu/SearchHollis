# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-28 10:39:02
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-06-29 09:32:18
from data_structures.data_structures import Payload
from fuzzywuzzy import fuzz
import helpers
from .match import match_isbn, match_title


def determinant(query_data: Payload, api_response) -> bool:
    """
    Algorithm:
    1. check isbn, if match ++, if not 0
    2. check title match, if match ++
    3. check author, if match ++

    Output: a confidence score out of 3.00 (3.00 = confident, 0.00 = no confidence)
            ideally should also return the fields where they don't match as notes
    """
    input_isbn = query_data.ISBN
    input_title_jpn = query_data.TITLE
    input_author_jpn = query_data.AUTHOR
    input_publisher_jpn = query_data.PUBLISHER
    input_pub_year = query_data.PUB_YEAR

    response_isbn = helpers.get_isbn_list(
        api_response["identifier"]
    )  # list of all isbn
    response_title_eng = api_response["titleInfo"][0]["title"]
    response_title_jpn = api_response["titleInfo"][1][
        "title"
    ]  # gives the title in Japanese
    response_author_eng = api_response["name"][0]["namePart"][0]
    response_author_jpn = api_response["name"][1]["namePart"][0]
    response_publisher_eng = api_response["originInfo"][0]["publisher"]
    response_publisher_jpn = api_response["originInfo"][1]["publisher"]
    response_pub_year = api_response["originInfo"][0]["dateIssued"]
    response_where = (api_response["location"][0]["physicalLocation"]["#text"]).split(
        ","
    )

    match_title(input_title_jpn, response_title_jpn)

    return match_isbn(input_isbn, response_isbn) or match_title(
        input_title_jpn, response_title_eng
    )
