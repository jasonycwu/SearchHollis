# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-29 08:38:42
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-06-29 09:43:56

from fuzzywuzzy import fuzz


def match_isbn(input_isbn, response_isbn):
    return input_isbn in response_isbn


def match_title(input_title, response_title):
    print(input_title, response_title)
    ratio_results = [
        fuzz.ratio(input_title, response_title),  # 100 if completely, general check
        fuzz.token_set_ratio(
            input_title, response_title
        ),  # ignore order and duplicates
        fuzz.token_sort_ratio(input_title, response_title),  # ignore word oder
        fuzz.partial_ratio(input_title, response_title),  # 100 if is a substring
    ]
    print(ratio_results)
    if any(condition == 100 for condition in ratio_results):
        return True
    else:
        return False

    print(fuzz.ratio(test, response_title))
    print(fuzz.token_set_ratio(test, response_title))
    print(fuzz.token_sort_ratio(test, response_title))
    print(fuzz.partial_ratio(test, response_title))  # works well for substring
