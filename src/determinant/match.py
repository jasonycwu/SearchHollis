# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-29 08:38:42
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-05 10:40:44

from fuzzywuzzy import fuzz
from typing import List


def match_isbn(input_isbn, response_isbn):
    """
    Checks whether input title and response title have the same ISBN by checking
    that input ISBN is one of the ISBNs listed in Harvard database
    """
    if response_isbn != None:
        return input_isbn in response_isbn


def match_title(input_title, response_title_list: List):
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
        ratio_results = [
            fuzz.ratio(input_title, response_title),  # 100 if completely, general check
            fuzz.token_set_ratio(
                input_title, response_title
            ),  # ignore order & duplicates
            fuzz.token_sort_ratio(input_title, response_title),  # ignore word oder
            fuzz.partial_ratio(input_title, response_title),  # 100 if is a substring
        ]
        if any(condition == 100 for condition in ratio_results):
            title_check_list.append(True)
        else:
            title_check_list.append(False)

    return any(condition == True for condition in title_check_list)
    print(fuzz.ratio(test, response_title))
    print(fuzz.token_set_ratio(test, response_title))
    print(fuzz.token_sort_ratio(test, response_title))
    print(fuzz.partial_ratio(test, response_title))  # works well for substring


def match_author():
    """
    Checks whether input title and response title have the same author
    """
    pass


def match_publication():
    """
    Checks whether input title and response title have the same publisher and
    publication year
    """
    pass
