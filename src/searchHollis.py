# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:18:58
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-08-13 13:35:10

import sys
import os

from src.data_structures.data_structures import Payload
from src.searches.isbn_search import search_by_isbn
from src.searches.title_search import search_by_title
from src.configs.configs import Configs
from src.input_output import extract_input_payload
from csv import writer, reader


def searchHollis(input_file, output_file, column_indices):
    found = 0
    header_row = True

    col_indices = {
        "ISBN": ord(column_indices["ISBN"].upper()) - 65,
        "TITLE": ord(column_indices["TITLE"].upper()) - 65,
        "AUTHOR": ord(column_indices["AUTHOR"].upper()) - 65,
        "PUBLISHER": ord(column_indices["PUBLISHER"].upper()) - 65,
        "PUB_YEAR": ord(column_indices["PUB_YEAR"].upper()) - 65,
    }

    with open(input_file, "r") as read_obj, open(
        output_file, "w", newline=""
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

                    if isbn_search_result["item_location"] == None:
                        result[0] = f"Held Online; Not in Widener/Yenching"
                    else:
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
                        if title_search_result["item_location"] == None:
                            result[0] = f"Held Online; Not in Widener/Yenching"
                        else:
                            result[
                                0
                            ] = f"Held in {title_search_result['item_location']}"

                        if title_search_result["permalink"]:
                            result[1] = title_search_result["permalink"]
                    else:
                        print(f"--NOT found (ISBN and TITLE)")
                csv_writer.writerow(result + row)
                print()
