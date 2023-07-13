# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:38:08
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-11 13:25:02
from typing import List
import dateparser


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


def get_response_publish_info(api_response):
    names_and_years = []
    if "originInfo" in api_response:
        originInfo = api_response["originInfo"]
        if isinstance(originInfo, List):
            for name in originInfo:
                if "publisher" in name and "dateIssued" in name:
                    pub_year = get_pub_year(name["dateIssued"])
                    names_and_years.append([name["publisher"], pub_year])
        else:
            if "publisher" in originInfo and "dateIssued" in originInfo:
                names_and_years.append(
                    [originInfo["publisher"], originInfo["dateIssued"]]
                )
    return names_and_years


def get_pub_year(dateIssued):
    """
    pass in name["dateIssued]
    can be a list or can be a dict
    """
    if isinstance(dateIssued, List):
        for item in dateIssued:
            if isinstance(item, dict) and "#text" in item:
                return item["#text"]
    else:
        return dateIssued


def get_isbn_list(response_identifier_field: List[dict]) -> List:
    if response_identifier_field:
        if type(response_identifier_field) == dict:
            response_identifier_field = [response_identifier_field]
        return [
            item.get("#text")
            for item in response_identifier_field
            if item and "#text" in item
        ]
    else:
        return []


def get_titles_list(response_identifier_field: List[dict]) -> List:
    if type(response_identifier_field) == dict:
        response_identifier_field = [response_identifier_field]
    return [item["title"] for item in response_identifier_field]


def get_author_names_list(response_identifier_field: List[dict]) -> List:
    names = []
    if type(response_identifier_field) == dict:
        response_identifier_field = [response_identifier_field]
    for item in response_identifier_field:
        if isinstance(item["namePart"], List):
            names.append(item["namePart"][0])
        else:
            names.append(item["namePart"])
    return names
