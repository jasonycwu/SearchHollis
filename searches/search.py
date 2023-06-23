import requests
import json

# general search function using a given request_url
def search(request_url):
        try:
            response = requests.get(request_url) # hit harvard api
            if response.status_code == 200:      # api hit success
                response = (json.loads(response.content)) # convert to Python dict
        except requests.exceptions.RequestException as e:
            print(response.status_code)
            print(f"Error: {e}")
        return response

def have_results(response: dict):
        if (response["pagination"]["numFound"] != 0) and (response["items"] != None):
            print("have data")
        else:
            print("no data") 

# checks if there is a match by comparing payload to responses
def have_match() -> bool:
    pass