# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:33:18
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-04 11:44:56
import json
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
def get_input(filename) -> list:
    with open(filename) as file:
        lines = file.readlines()
    return lines


def extract_input_payload(input_data) -> Payload:
    all_title_names = [input_data[1]] + input_data[1].split(" ")
    extracted_input = Payload(
        format_isbn(input_data[0]),  # ISBN, will need a list
        input_data[1],  # TITLE
        input_data[2],  # AUTHOR, will need a list
        input_data[3],  # PUBLISHER
        input_data[4],  # PUB YEAR
        all_title_names,  # list of TITLE broken down
    )
    return extracted_input
