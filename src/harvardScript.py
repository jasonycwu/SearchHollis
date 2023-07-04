# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:18:58
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-04 12:09:59
import json
import requests
from dataclasses import dataclass

from data_structures.data_structures import Payload
from searches.isbn_search import search_by_isbn
from searches.title_search import search_by_title
from configs.configs import Configs
from input_output import writeToFile, get_input, extract_input_payload

if __name__ == "__main__":
    input_data = get_input(Configs.TEST_IUTPUT_TXT_PATH)  # test multiple input
    # input_data = get_input(Configs.SINGLE_INPUT_TXT_PATH)  # test a single input

    # going title by title from the input list
    for item in input_data:
        item = item.split(",")
        payload = extract_input_payload(item)
        print(payload.FULL_TITLE)

        if search_by_isbn(payload):
            print(f".................. FOUND at Harvard by isbn")
        elif search_by_title(payload):
            print(f".................. FOUND by title")
        else:
            print(f".................. NOT found at Harvard by isbn and title")
        print()
