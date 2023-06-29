# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:56:17
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-06-29 00:57:08
from configs.configs import Configs


# wrapper function to search by title
# INPUT     search field title
# OUTPUT    response
def search_by_title(self, title):
    title_field = f"q={title}"
    request_url = Configs.BASE_URL + f"{title_field}&limit=5"

    response = self.search(request_url)
    return response

    self.have_results(response)
    result_list = response["items"]["mods"]
    print(len(result_list))
    self.writeToFile(response)
    # TODO: DETERMINE MATCH
