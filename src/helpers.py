# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:38:08
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-04 10:45:28
from typing import List


def format_isbn(isbn_string):
    isbn = isbn_string.replace("-", "")
    return isbn


def get_isbn_list(response_identifier_field: List[dict]) -> List:
    if type(response_identifier_field) == dict:
        response_identifier_field = [response_identifier_field]
    return [item["#text"] for item in response_identifier_field]


def get_titles_list(response_identifier_field: List[dict]) -> List:
    if type(response_identifier_field) == dict:
        response_identifier_field = [response_identifier_field]
    return [item["title"] for item in response_identifier_field]


def get_author_names_list(response_identifier_field: List[dict]) -> List:
    if type(response_identifier_field) == dict:
        response_identifier_field = [response_identifier_field]
    return [item["namePart"][0] for item in response_identifier_field]
