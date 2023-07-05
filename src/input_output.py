# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:33:18
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-05 02:54:49
import json
import math
import pandas as pd
from data_structures.data_structures import Payload
from helpers import format_isbn
from configs.configs import Configs


# write some data to a txt file
def writeToFile(data) -> None:
    formatted = json.dumps(data, indent=2)
    try:
        with open(Configs.TEST_OUTPUT_TXT_PATH, "w+") as file:
            file.write(formatted)
    except:
        print(f"Error")


# gets all the items (titles) from an input file
def get_input(filename):
    df = pd.read_csv(filename)
    cols_to_keep = ["ISBN", "Title", "Author", "Publisher", "Year Published"]
    df = df[cols_to_keep]
    return df


def get_input_from_csv(filename) -> list:
    with open(filename) as file:
        lines = file.readlines()
    return lines


def extract_input_payload(input_data) -> Payload:
    isbn = input_data["ISBN"]
    title = input_data["Title"]
    author = input_data["Author"]
    publisher = input_data["Publisher"]
    pub_year = input_data["Year Published"]

    # gets the full title itself, and diff components of the full title
    all_title_parts = [t for t in ([title] + title.split(" ")) if len(t) >= 2]

    # breaks down and groups all author name
    if type(author) is not float:
        authors = [t for t in ([author[0]] + author.split(" ")) if len(t) >= 2]
        # print(authors)
    else:
        authors = [""]

    extracted_input = Payload(
        format_isbn(str(isbn)),  # ISBN
        title,  # TITLE
        authors[0],  # AUTHOR, will need a list
        publisher,  # PUBLISHER
        str(pub_year),  # PUB YEAR
        all_title_parts,  # list of TITLE broken down
    )
    return extracted_input
