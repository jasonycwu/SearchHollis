# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:38:08
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-05 11:01:15
from typing import List


def format_isbn(isbn_string):
    isbn = isbn_string.replace("-", "")
    return isbn


def get_response_titles(api_response):
    if "titleInfo" in api_response:
        response_titles = get_titles_list(api_response["titleInfo"])
    else:
        response_titles = ""
    return response_titles


def get_response_isbn(api_response):
    if "identifier" in api_response:
        response_isbn = get_isbn_list(api_response["identifier"])
    else:
        response_isbn = ""
    return response_isbn


def get_response_author_names(api_response):
    if "name" in api_response:
        response_author_names = get_author_names_list(api_response["name"])
    else:
        response_author_names = ""
    return response_author_names


def get_response_publisher_names():
    pass


def get_response_pub_year():
    pass


def get_isbn_list(response_identifier_field: List[dict]) -> List:
    if type(response_identifier_field) == dict:
        response_identifier_field = [response_identifier_field]
    return [
        item.get("#text")
        for item in response_identifier_field
        if item and "#text" in item
    ]


def get_titles_list(response_identifier_field: List[dict]) -> List:
    if type(response_identifier_field) == dict:
        response_identifier_field = [response_identifier_field]
    return [item["title"] for item in response_identifier_field]


def get_author_names_list(response_identifier_field: List[dict]) -> List:
    if type(response_identifier_field) == dict:
        response_identifier_field = [response_identifier_field]
    return [item["namePart"][0] for item in response_identifier_field]
