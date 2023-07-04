# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-29 08:38:42
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-04 11:57:02

from fuzzywuzzy import fuzz
from typing import List


def match_isbn(input_isbn, response_isbn):
    if response_isbn != None:
        return input_isbn in response_isbn


# TODO: check authors too
def match_title(input_title, response_title_list: List):
    title_check_list = []
    for response_title in response_title_list:
        ratio_results = [
            fuzz.ratio(input_title, response_title),  # 100 if completely, general check
            fuzz.token_set_ratio(
                input_title, response_title
            ),  # ignore order and duplicates
            fuzz.token_sort_ratio(input_title, response_title),  # ignore word oder
            fuzz.partial_ratio(input_title, response_title),  # 100 if is a substring
        ]
        # print(f"{input_title} and {response_title} result={ratio_results}")
        if any(condition == 100 for condition in ratio_results):
            title_check_list.append(True)
        else:
            title_check_list.append(False)

    if any(condition == True for condition in title_check_list):
        return True
    else:
        return False

    print(fuzz.ratio(test, response_title))
    print(fuzz.token_set_ratio(test, response_title))
    print(fuzz.token_sort_ratio(test, response_title))
    print(fuzz.partial_ratio(test, response_title))  # works well for substring
