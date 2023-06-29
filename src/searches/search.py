# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:29:05
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-06-29 00:52:48
import requests
import json


# general search function using a given request_url
def search(request_url):
    try:
        response = requests.get(request_url)  # hit harvard api
        if response.status_code == 200:  # api hit success
            response = json.loads(response.content)  # convert to Python dict
    except requests.exceptions.RequestException as e:
        print(response.status_code)
        print(f"Error: {e}")
    return response


# checks if response from API is empty
def have_results(response: dict):
    return (response["pagination"]["numFound"] != 0) and (response["items"] != None)


# checks if there is a match by comparing payload to responses
def have_match() -> bool:
    pass
