# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:22:51
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-11 15:09:12
# from harvardScript import BASE_URL
from configs.configs import Configs
from input_output import writeToFile
from determinant.determinant import determinant, held_at_harvard
from data_structures.data_structures import Payload
from searches import search, have_results


# wrapper function to search by isbn
# for each of the search modules:
#   INPUT:  search fields isbn
#   OUT:    response
def search_by_isbn(payload: Payload):
    """
    INPUT= payload, aka extracted data from input
    OUTPUT= bool whether a correct match is found

    Algorithm:
    1. extract relevant fields and form request url
    2. use url to get response from Harvard
    3. if there are results throw it in the Determinant and return a confidence score
    4. if determinant meets threshhold, return match
        false otherwise
    """
    print("SEARCHING BY ISBN")

    isbn_field = f"identifier={payload.ISBN}"
    request_url = Configs.BASE_URL + f"{isbn_field}"
    response = search(request_url)
    num_of_results = have_results(response)
    writeToFile(response)

    if num_of_results == 1:
        response_item = response["items"]["mods"]
        if determinant(query_data=payload, api_response=response_item):  # same bok
            return held_at_harvard(api_response=response_item)
        else:  # not same bok
            return None
    else:
        return None
