# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:18:58
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-05 10:37:55

from data_structures.data_structures import Payload
from searches.isbn_search import search_by_isbn
from searches.title_search import search_by_title
from configs.configs import Configs
from input_output import (
    writeToFile,
    get_input,
    extract_input_payload,
    get_input_from_csv,
)

INPUT_ROOT = "/Users/jasonycwu/Documents/GitHub/harvardScript/input"

if __name__ == "__main__":
    input_data = get_input(
        "/Users/jasonycwu/Documents/GitHub/harvardScript/tests/input/complex-pagination.csv"
    )
    query_count = 0

    # going title by title from the input list
    for item in input_data.iterrows():
        payload = extract_input_payload(item[1])
        print("input:", payload.FULL_TITLE)
        query_count += 1

        if search_by_isbn(payload):
            print(f".................. FOUND at Harvard by isbn")
        elif search_by_title(payload):
            query_count += 1
            print(f".................. FOUND by title")
        else:
            query_count += 1
            print(f".................. NOT found at Harvard by isbn and title")

        print("Query count: ", query_count)
        print()
