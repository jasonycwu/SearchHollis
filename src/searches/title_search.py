# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:56:17
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-04 12:09:22
from configs.configs import Configs
from input_output import writeToFile
from determinant.determinant import determinant, held_at_harvard
from data_structures.data_structures import Payload
from searches import search, have_results


def search_by_title(payload: Payload):
    print("SEARCHING BY TITLE")
    for title in payload.TITLES:
        # print("searching with 「", title, "」")

        title_field = f"q={title}"
        request_url = Configs.BASE_URL + f"{title_field}"
        response = search(request_url)
        response_pagination = response["pagination"]
        numFound = response_pagination["numFound"]
        num_of_results = have_results(response)
        writeToFile(response)

        if numFound != 0 and numFound != 1:
            response_items_list = response["items"]["mods"]
            for item in response_items_list:
                if determinant(query_data=payload, api_response=item):
                    return held_at_harvard(api_response=item)

    return None

    # response_items = response["items"]
    # if num_of_results != 0 and num_of_results != 1:  # max 10 by default
    #     response_items_list = response["items"]["mods"]
    #     print(len(response_items_list))

    #     for item in response_items_list:
    #         pass
    # print(determinant(query_data=payload, api_response=item))
    # writeToFile(item)  # delete later

    # print(len(response_items_list))
    # print(f"there are {num_of_results} results")

    # if num_of_results != 0:
    #     if num_of_results == 1:  # one found
    #         response_items = [response["items"]["mods"]]
    #     else:  # more than one found
    #         response_items = response["items"]["mods"]

    #     if determinant(query_data=payload, api_response=response_items):
    #         return True
    #     else:
    #         return False
    # else:
    #     return None


# def search_by_title_old(self, title):
#     title_field = f"q={title}"
#     request_url = Configs.BASE_URL + f"{title_field}&limit=5"

#     response = self.search(request_url)
#     return response

#     self.have_results(response)
#     result_list = response["items"]["mods"]
#     print(len(result_list))
#     self.writeToFile(response)
#     # TODO: DETEMINE MATCH
