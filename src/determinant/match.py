# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-29 08:38:42
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-10 08:11:07

from fuzzywuzzy import fuzz
from typing import List


def match_isbn(input_isbn, response_isbn) -> bool:
    """
    Checks whether input title and response title have the same ISBN by checking
    that input ISBN is one of the ISBNs listed in Harvard database
    """
    if response_isbn != None:
        if (input_isbn in response_isbn) or (
            any(fuzz.partial_ratio(input_isbn, isbn) == 100 for isbn in response_isbn)
        ):
            # print("     match_isbn-ISBN MATCH")
            return True
        else:
            # print("     match_isbn-ISBN NOT MATCH")
            return False
    return False
    return input_isbn in response_isbn


def match_title(input_title, response_title_list: List) -> bool:
    """
    Checks whether input title and response title have the same title
    takes in input query title and a list of title names from Harvard database
    For every title in the list of title names:
    1. if input matches with title from response, append to checklist
        else, append false
    2. if checklist contains any matches, return true
    """
    title_check_list = []
    for response_title in response_title_list:
        # print(f"    {response_title}")
        ratio_results = [
            fuzz.ratio(input_title, response_title),  # 100 if completely, general check
            fuzz.token_set_ratio(
                input_title, response_title
            ),  # ignore order & duplicates
            fuzz.token_sort_ratio(input_title, response_title),  # ignore word oder
            fuzz.partial_ratio(input_title, response_title),  # 100 if is a substring
        ]
        if any(condition >= 90 for condition in ratio_results):
            title_check_list.append(True)
        else:
            title_check_list.append(False)

    if any(condition == True for condition in title_check_list):
        # print("     match_title-TITLE MATCH")
        return True
    else:
        # print("     match_title-TITLE NOT MATCH")
        return False
    return any(condition == True for condition in title_check_list)


def match_author(input_author, response_authors: List):
    """
    Checks whether input title and response title have the same author
    """
    results = []
    for name in response_authors:
        ratio_results = [
            fuzz.ratio(input_author, name),  # 100 if completely, general check
            fuzz.token_set_ratio(input_author, name),  # ignore order & duplicates
            fuzz.token_sort_ratio(input_author, name),  # ignore word oder
            fuzz.partial_ratio(input_author, name),  # 100 if is a substring
        ]
        if any(condition >= 90 for condition in ratio_results):
            results.append(True)
        else:
            results.append(False)

    if any(condition == True for condition in results):
        # print("     match_author-AUTHOR MATCH")
        return True
    else:
        # print("     match_author-WRONG AUTHOR")
        return False
    return any(condition == True for condition in results)


def match_publication(publisher, pub_year, response_pub_info):
    """
    Checks whether input title and response title have the same publisher and
    publication year
    """
    if response_pub_info != []:
        response_year = response_pub_info[0][1]
        year_match = fuzz.partial_ratio(pub_year, response_year)
        results = []
        for item in response_pub_info:
            ratio_results = [
                fuzz.ratio(publisher, item[0]),
                fuzz.token_set_ratio(publisher, item[0]),
                fuzz.token_sort_ratio(publisher, item[0]),
                fuzz.partial_ratio(publisher, item[0]),
            ]
            if any(condition >= 90 for condition in ratio_results):
                results.append(True)
            else:
                results.append(False)

        if any(condition == True for condition in results) and year_match >= 90:
            # print("     match_publication-PUBLISHER AND YEAR MATCH")
            return True
        elif any(condition == True for condition in results):
            # print("     match_publication-PUBLISHER MATCH ONLY, wrong year")
            return False
        else:
            # print("     match_publication-NO PUB MATCH")
            return False
    return False
