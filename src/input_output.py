# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:33:18
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-08-13 13:22:10
import json
import math
import pandas as pd
from src.data_structures.data_structures import Payload
from src.helpers import format_isbn
from src.configs.configs import Configs


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
    return df


def get_authors(author):
    authors = []
    if author:
        for name in author.split(" "):
            if len(name) >= 2:
                authors.append(name)
    if len(authors) == 0:
        authors.append("")
    return authors


def extract_input_payload(input_data, col_indices) -> Payload:
    isbn = input_data[col_indices["ISBN"]]
    title = input_data[col_indices["TITLE"]]
    author = input_data[col_indices["AUTHOR"]]
    publisher = input_data[col_indices["PUBLISHER"]]
    pub_year = input_data[col_indices["PUB_YEAR"]]

    # gets the full title itself, and diff components of the full title
    if title == title.split(" ")[0]:
        all_title_parts = [title]
    else:
        all_title_parts = [title, title.split(" ")[0]]

    authors = get_authors(author)

    extracted_input = Payload(
        format_isbn(str(isbn)),  # ISBN
        title,  # TITLE
        authors,  # AUTHOR, will need a list
        publisher,  # PUBLISHER
        str(pub_year),  # PUB YEAR
        all_title_parts,  # list of TITLE broken down
    )
    return extracted_input
