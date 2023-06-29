# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:38:08
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-06-29 08:38:10
from typing import List


def format_isbn(isbn_string):
    isbn = isbn_string.replace("-", "")
    return isbn


def get_isbn_list(response_identifier_field: List[dict]) -> List:
    return [item["#text"] for item in response_identifier_field]
