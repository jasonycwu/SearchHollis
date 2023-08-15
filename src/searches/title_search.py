# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:56:17
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-08-15 16:38:42
from src.configs.configs import Configs
from src.input_output import writeToFile
from src.determinant.determinant import determinant, held_at_harvard
from src.data_structures.data_structures import Payload
from src.searches import search, have_results


def search_by_title(payload: Payload, SEARCH_INDEX):
    """
    Return      [result, SEARCH_INDEX]
    """
    print("SEARCHING BY TITLE")
    for title in payload.TITLES:
        title_field = f"q={title}"
        request_url = Configs.BASE_URL + f"{title_field}&limit=10"
        response = search(request_url)
        if response == "LIMIT":  # Harvard API Limit Reached
            return ["LIMIT", SEARCH_INDEX]
        SEARCH_INDEX += 1
        numFound = have_results(response)

        if numFound != 0 and numFound != 1:
            response_items_list = response["items"]["mods"]
            for item in response_items_list:
                if determinant(query_data=payload, api_response=item):
                    return [held_at_harvard(api_response=item), SEARCH_INDEX]
    return [None, SEARCH_INDEX]
