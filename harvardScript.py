import json
import requests
from dataclasses import dataclass
from data_structures.data_structures import Payload
from searches.isbn_search import search_by_isbn
from configs.configs import Configs
from input_output import writeToFile, get_input, extract_input_payload

if __name__ == '__main__':
    input_data = (get_input('testInput.txt')) # list of input items
    # going title by title
    for item in input_data:
        item = item.split(',')
        payload = extract_input_payload(item)
        
        response = search_by_isbn(payload.ISBN)
        # harvard_script.have_results(response)
        # print(response)
        # ISBN Search
        

        # Title Search
        # harvard_script.search_by_title(payload.TITLE)

        # TODO: if no result, author search
        # item = item.split(',')
        # harvard_script.form_query(item)

