# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:18:58
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-08-15 16:38:00

import sys
import os

from src.data_structures.data_structures import Payload
from src.searches.isbn_search import search_by_isbn
from src.searches.title_search import search_by_title
from src.configs.configs import Configs
from src.input_output import extract_input_payload
from csv import writer, reader


def searchHollis(input_file, output_file, BOOK_COUNT, column_indices):
    SEARCH_INDEX = 0  # receive from flask app
    SEARCH_CEILING = SEARCH_INDEX + 200
    BOOK_COUNT = BOOK_COUNT
    header = True  # flag for header row

    # convert column indices
    col_indices = {
        "ISBN": ord(column_indices["ISBN"].upper()) - 65,
        "TITLE": ord(column_indices["TITLE"].upper()) - 65,
        "AUTHOR": ord(column_indices["AUTHOR"].upper()) - 65,
        "PUBLISHER": ord(column_indices["PUBLISHER"].upper()) - 65,
        "PUB_YEAR": ord(column_indices["PUB_YEAR"].upper()) - 65,
    }

    with open(input_file, "r") as read_obj, open(
        output_file, "a", newline=""
    ) as write_obj:
        # initialize reader and writer
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)

        # skip through rows based on index
        for _ in range(BOOK_COUNT):  # skip lines until start index
            # print("in here")
            next(csv_reader, None)

        for row in csv_reader:
            if SEARCH_INDEX >= SEARCH_CEILING:
                return ["CONTINUE", BOOK_COUNT]

            if header == True and BOOK_COUNT == 0:
                # header row, append two extra cols at front
                print("creating header.")
                header = ["HELD AT HARVARD", "HARVARD PERMALINK"] + row
                csv_writer.writerow(header)
                header = False
            else:
                # initalize columns to append to file
                result = ["Not Found", "No Permalink Found"]

                payload = extract_input_payload(row, col_indices)
                print(f"INPUT--「{payload.FULL_TITLE}」")
                print(
                    f"       {payload.ISBN}, {payload.AUTHOR}, {payload.PUBLISHER}, {payload.PUB_YEAR}"
                )

                isbn_search_result = search_by_isbn(payload, SEARCH_INDEX)
                SEARCH_INDEX = isbn_search_result[1]
                # print(SEARCH_INDEX)
                if isbn_search_result[0]:
                    if isbn_search_result[0] == "LIMIT":  # quit due to API limit
                        return ["LIMIT", BOOK_COUNT]
                    print(f"--FOUND by ISBN: {isbn_search_result[0]['item_location']}")

                    if isbn_search_result[0]["item_location"] == None:
                        result[0] = f"Held Online; Not in Widener/Yenching"
                    else:
                        result[0] = f"Held in {isbn_search_result[0]['item_location']}"

                    if isbn_search_result[0]["permalink"]:
                        result[1] = isbn_search_result[0]["permalink"]
                else:
                    title_search_result = search_by_title(payload, SEARCH_INDEX)
                    SEARCH_INDEX = title_search_result[1]
                    # print(SEARCH_INDEX)
                    if title_search_result[0]:
                        if title_search_result[0] == "LIMIT":  # quit due to API limit
                            return ["LIMIT", BOOK_COUNT]
                        print(
                            f"--FOUND by TITLE {title_search_result[0]['item_location']}"
                        )
                        if title_search_result[0]["item_location"] == None:
                            result[0] = f"Held Online; Not in Widener/Yenching"
                        else:
                            result[
                                0
                            ] = f"Held in {title_search_result[0]['item_location']}"

                        if title_search_result[0]["permalink"]:
                            result[1] = title_search_result[0]["permalink"]
                    else:
                        print(f"--NOT found (ISBN and TITLE)")
                BOOK_COUNT += 1
                csv_writer.writerow(result + row)
                print()
        return ["COMPLETE", BOOK_COUNT]


"""
RETURNS:
- "CONTINUE" -> the most recent search index
- "COMPLETE" -> the file has been completed
- "LIMIT" -> Harvard API Limit reached, go into waiting
- tbd: "ERROR" -> handle errors?
"""
