import json
import requests
from dataclasses import dataclass
from data_structures import Payload

BASE_URL = "https://api.lib.harvard.edu/v2/items.json?"
LIMIT = 5

class HarvardScript:
    def __init__(self) -> None:
        pass

    # write some data to a txt file
    def writeToFile(self, data) -> None:
        formatted = json.dumps(data, indent=2)
        try:
            with open('/Users/jasonycwu/Desktop/HarvardScript/testOutput.txt', 'w+') as file:
                file.write(formatted)
        except:
            print(f"Error")
        
    # gets all the items (titles) from an input file
    def get_input(self, filename) -> list:
        with open(filename) as file:
            lines = file.readlines()
        return lines
    
    # # constructs a request url for LibraryCloud using payload
    # def form_query(self, isbn) -> str:
    #     isbn_field = f"identifier={isbn}"
    #     request_url = BASE_URL + f"{isbn_field}&"
    #     return request_url
    
    # extracts relevant fields and construct a payload object
    def extract_input_payload(self, input_data) -> Payload:
        print(input_data)
        extracted_input = Payload(
            self.format_isbn(input_data[0]),    # ISBN, will need a list
            input_data[1],                      # TITLE
            input_data[2],                      # AUTHOR, will need a list
            input_data[3],                      # PUBLISHER
            input_data[4],                      # PUB YEAR
        )
        return extracted_input
    
    def have_results(self, response: dict):
        if (response["pagination"]["numFound"] != 0) and (response["items"] != None):
            print("have data")
        else:
            print("no data")

    # checks if there is a match by comparing payload to responses
    def have_match(self) -> bool:
        pass

    # general search function using a given request_url
    def search(self, request_url):
        try:
            response = requests.get(request_url) # hit harvard api
            if response.status_code == 200:      # api hit success
                response = (json.loads(response.content)) # convert to Python dict
        except requests.exceptions.RequestException as e:
            print(response.status_code)
            print(f"Error: {e}")
        return response

    # wrapper function to search by isbn
    # for each of the search modules:
    #   INPUT:  search fields isbn
    #   OUT:    response
    def search_by_isbn(self, isbn):
        isbn_field = f"identifier={isbn}"
        request_url = BASE_URL + f"{isbn_field}"

        response = self.search(request_url)
        self.writeToFile(response) #delete later
        
        if (self.have_results(response)):
            # TODO: DETERMINE MATCH
            pass
        else:
            # return no match found
            pass
        return response        
        

    def format_isbn(self, isbn_string):
        isbn = isbn_string.replace("-", "")
        return isbn

    # wrapper function to search by title
    # INPUT     search field title
    # OUTPUT    response
    def search_by_title(self, title):
        title_field = f"q={title}"
        request_url = BASE_URL + f"{title_field}&limit=5"
        
        response = self.search(request_url)
        return response

        self.have_results(response)
        result_list = response["items"]["mods"]
        print(len(result_list))
        self.writeToFile(response)
        # TODO: DETERMINE MATCH
        
    def search_by_author(self):
        pass
    
if __name__ == '__main__':
    harvard_script = HarvardScript()
    input_data = (harvard_script.get_input('testInput.txt')) # list of input items
    # going title by title
    for item in input_data:
        item = item.split(',')
        payload = harvard_script.extract_input_payload(item)
        
        response = harvard_script.search_by_isbn(payload.ISBN)
        # harvard_script.have_results(response)
        # print(response)
        # ISBN Search
        

        # Title Search
        # harvard_script.search_by_title(payload.TITLE)

        # TODO: if no result, author search
        # item = item.split(',')
        # harvard_script.form_query(item)

