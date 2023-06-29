# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:22:51
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-06-29 02:11:07
# from harvardScript import BASE_URL
from configs.configs import Configs
from .search import search, have_results
from input_output import writeToFile
from .determinant import determinant
from data_structures.data_structures import Payload


# wrapper function to search by isbn
# for each of the search modules:
#   INPUT:  search fields isbn
#   OUT:    response
def search_by_isbn(payload: Payload):
    """
    INPUT= payload, aka extracted data from input
    OUTPUT=

    Algorithm:
    1. extract relevant fields and form request url
    2. use url to get response from Harvard
    3. if there are results throw it in the Determinant and return a confidence score
    4. if determinant meets threshhold, return match
        false otherwise
    """
    isbn_field = f"identifier={payload.ISBN}"
    request_url = Configs.BASE_URL + f"{isbn_field}"

    response = search(request_url)
    writeToFile(response)  # delete later

    if have_results(response):
        response = response["items"]["mods"]
        confidence = determinant(query_data=payload, api_response=response)
        # TODO: DETERMINE MATCH (code Determinant)
        pass
    else:
        # return, no results found
        return None
    return response
