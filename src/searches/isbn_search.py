# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:22:51
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-08-15 07:44:07
# from harvardScript import BASE_URL
from src.configs.configs import Configs
from src.input_output import writeToFile
from src.determinant.determinant import determinant, held_at_harvard
from src.data_structures.data_structures import Payload
from src.searches import search, have_results


# wrapper function to search by isbn
# for each of the search modules:
#   INPUT:  search fields isbn
#   OUT:    response
def search_by_isbn(payload: Payload, SEARCH_INDEX):
    """
    Return      [result, SEARCH_INDEX]
    """
    print("SEARCHING BY ISBN")

    isbn_field = f"identifier={payload.ISBN}"
    request_url = Configs.BASE_URL + f"{isbn_field}"
    response = search(request_url)
    if response == "LIMIT":  # Harvard API Limit Reached
        return ["LIMIT", SEARCH_INDEX]
    SEARCH_INDEX += 1
    num_of_results = have_results(response)

    if num_of_results == 1:
        response_item = response["items"]["mods"]
        if determinant(query_data=payload, api_response=response_item):  # same bok
            return [held_at_harvard(api_response=response_item), SEARCH_INDEX]
        else:  # not same bok
            return [None, SEARCH_INDEX]
    else:
        return [None, SEARCH_INDEX]
