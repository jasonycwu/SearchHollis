# from harvardScript import BASE_URL
from configs.configs import Configs
from searches.search import search, have_results
from input_output import writeToFile
# wrapper function to search by isbn
    # for each of the search modules:
    #   INPUT:  search fields isbn
    #   OUT:    response
def search_by_isbn(isbn):
        isbn_field = f"identifier={isbn}"
        request_url = Configs.BASE_URL + f"{isbn_field}"

        response = search(request_url)
        writeToFile(response) #delete later
        
        if (have_results(response)):
            # TODO: DETERMINE MATCH
            pass
        else:
            # return no match found
            pass
        return response 