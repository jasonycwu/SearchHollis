# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:18:58
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-10 08:50:03

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
import csv

INPUT_ROOT = "/Users/jasonycwu/Documents/GitHub/harvardScript/input"

if __name__ == "__main__":
    input_data = get_input(
        "/Users/jasonycwu/Documents/GitHub/harvardScript/tests/input/to-search-official.csv"
    )
    query_count = 0
    found = 0
    total_items_num = 0

    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        header = ["ISBN", "TITLE", "AUTHOR", "PUBLISHER", "YEAR"]
        writer.writerow(header)
        # going title by title from the input list
        for item in input_data.iterrows():
            total_items_num += 1
            payload = extract_input_payload(item[1])
            print(f"INPUT--「{payload.FULL_TITLE}」")
            print(
                f"       {payload.ISBN}, {payload.AUTHOR}, {payload.PUBLISHER}, {payload.PUB_YEAR}"
            )
            row = [
                payload.ISBN,
                payload.FULL_TITLE,
                payload.AUTHOR,
                payload.PUBLISHER,
                payload.PUB_YEAR,
            ]
            query_count += 1
            isbn_search_result = search_by_isbn(payload)
            title_search_result = search_by_title(payload)

            if isbn_search_result:
                found += 1
                # print(f"--FOUND by ISBN: {isbn_search_result}")
                row = row + [f"Held in {isbn_search_result}"]
            elif title_search_result:
                found += 1
                query_count += 1
                # print(f"--FOUND by TITLE {title_search_result}")
                row = row + [f"Held in {title_search_result}"]
            else:
                query_count += 1
                # print(f"--NOT found (ISBN and TITLE)")
                row = row + [f"Not Found"]

            writer.writerow(row)
            print()
            # if query_count >= 100:
            #     break

        # print(f"TOTAL ITEMS SEARCHED: {total_items_num}")
        # print(f"NUM FOUND: {found}")
