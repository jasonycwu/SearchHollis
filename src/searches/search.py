# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:29:05
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-08-15 16:39:05
import requests
import json
import time


# general search function using a given request_url
def search(request_url):
    try:
        response = requests.get(request_url)  # hit harvard api
        print("search")
        if response.status_code == 403:
            return "LIMIT"
        if response.status_code == 200:  # api hit success
            response = json.loads(response.content)  # convert to Python dict
    except requests.exceptions.RequestException as e:
        print(response.status_code)
        print(f"Error: {e}")
    return response


# checks if response from API is empty
def have_results(response: dict):
    numFound = 0
    if isinstance(response, dict):
        pagination = response.get("pagination")
        numFound = pagination.get("numFound") if pagination else None
    return numFound
