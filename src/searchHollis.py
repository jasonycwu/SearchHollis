# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:18:58
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-19 11:11:10

from data_structures.data_structures import Payload
from searches.isbn_search import search_by_isbn
from searches.title_search import search_by_title
from configs.configs import Configs
from input_output import get_input, extract_input_payload
from csv import writer, reader

INPUT_ROOT = "/Users/jasonycwu/Documents/GitHub/harvardScript/input"
INPUT_FILE_PATH = (
    "/Users/jasonycwu/Documents/GitHub/harvardScript/tests/input/to-search-official.csv"
)

# main
if __name__ == "__main__":
    input_data = get_input(INPUT_FILE_PATH)
    found = 0
    total_items_num = 0
    header_row = True

    # TODO: eventually, users will specify these indices
    col_indices = {
        "ISBN": 3,
        "TITLE": 4,
        "AUTHOR": 5,
        "PUBLISHER": 7,
        "YEAR": 8,
    }

    with open(INPUT_FILE_PATH, "r") as read_obj, open(
        "output.csv", "w", newline=""
    ) as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)

        for row in csv_reader:
            if header_row == True:  # header row, append two extra cols at front
                header = ["HELD AT HARVARD", "HARVARD PERMALINK"] + row
                csv_writer.writerow(header)
                header_row = False
            else:
                result = ["Not Found", "No Permalink Found"]
                payload = extract_input_payload(row, col_indices)
                print(f"INPUT--「{payload.FULL_TITLE}」")
                print(
                    f"       {payload.ISBN}, {payload.AUTHOR}, {payload.PUBLISHER}, {payload.PUB_YEAR}"
                )

                isbn_search_result = search_by_isbn(payload)
                if isbn_search_result:
                    found += 1
                    print(f"--FOUND by ISBN: {isbn_search_result['item_location']}")
                    result[0] = f"Held in {isbn_search_result['item_location']}"
                    if isbn_search_result["permalink"]:
                        result[1] = isbn_search_result["permalink"]
                else:
                    title_search_result = search_by_title(payload)
                    if title_search_result:
                        found += 1
                        print(
                            f"--FOUND by TITLE {title_search_result['item_location']}"
                        )
                        result[0] = f"Held in {title_search_result['item_location']}"
                        if title_search_result["permalink"]:
                            result[1] = title_search_result["permalink"]
                    else:
                        print(f"--NOT found (ISBN and TITLE)")
                csv_writer.writerow(result + row)
                print()
