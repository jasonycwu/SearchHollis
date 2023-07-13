# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:56:17
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-13 16:56:32
from configs.configs import Configs
from input_output import writeToFile
from determinant.determinant import determinant, held_at_harvard
from data_structures.data_structures import Payload
from searches import search, have_results


def search_by_title(payload: Payload):
    print("SEARCHING BY TITLE")
    for title in payload.TITLES:
        title_field = f"q={title}"
        request_url = Configs.BASE_URL + f"{title_field}&limit=100"
        response = search(request_url)
        numFound = have_results(response)

        if numFound != 0 and numFound != 1:
            response_items_list = response["items"]["mods"]
            for item in response_items_list:
                if determinant(query_data=payload, api_response=item):
                    return held_at_harvard(api_response=item)
    return None
