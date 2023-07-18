# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:18:58
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-18 16:47:08

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
    found = 0
    total_items_num = 0

    # TODO: change such that the outputs are appended to the original file
    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        header = [
            "ISBN",
            "TITLE",
            "AUTHOR",
            "PUBLISHER",
            "YEAR",
            "FOUND/NOT FOUND",
            "LINK",
        ]
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
                "Not Found",
                "No Link",
            ]
            isbn_search_result = search_by_isbn(payload)

            if isbn_search_result:
                found += 1
                print(f"--FOUND by ISBN: {isbn_search_result['item_location']}")
                row[5] = f"Held in {isbn_search_result['item_location']}"
                if isbn_search_result["permalink"]:
                    row[6] = isbn_search_result["permalink"]
            else:
                title_search_result = search_by_title(payload)
                if title_search_result:
                    found += 1
                    print(f"--FOUND by TITLE {title_search_result['item_location']}")
                    row[5] = f"Held in {title_search_result['item_location']}"
                    if title_search_result["permalink"]:
                        row[6] = title_search_result["permalink"]
                else:
                    print(f"--NOT found (ISBN and TITLE)")

            writer.writerow(row)
            print()
