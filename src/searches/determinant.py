# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-28 10:39:02
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-06-29 01:35:10
from data_structures.data_structures import Payload
from fuzzywuzzy import fuzz


def determinant(query_data: Payload, api_response) -> int:
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

    response_isbn = api_response["identifier"]
    response_title_eng = api_response["titleInfo"][0]
    response_title_jpn = api_response["titleInfo"][1]  # gives the title in Japanese
    response_author_eng = api_response["name"][0]["namePart"][0]
    response_author_jpn = api_response["name"][1]["namePart"][0]
    response_publisher_eng = api_response["originInfo"][0]["publisher"]
    response_publisher_jpn = api_response["originInfo"][1]["publisher"]
    response_pub_year = api_response["originInfo"][0]["dateIssued"]

    print(f"INPUT: {input_publisher_jpn}")
    print(f"RESPONSE: {response_publisher_jpn}")
    test1 = "文芸春秋"
    test2 = "文 藝 春 秋"
    test3 = "春 秋"
    print(fuzz.ratio(input_publisher_jpn, test3))
    print(fuzz.token_set_ratio(input_publisher_jpn, test3))
    print(fuzz.token_sort_ratio(input_publisher_jpn, test3))
    print(fuzz.partial_ratio(input_publisher_jpn, test3))  # works well for substring

    #     if input_publisher_jpn == response_publisher_jpn:
    #         print("MATCH")

    confidence = 0
    return confidence
