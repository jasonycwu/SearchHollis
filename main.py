import requests
import json
import fileinput

def main():
    return 0

# wrapper function for book title search
def search_book_titles(query):
    base_url = "https://api.lib.harvard.edu/v2/items.json?"
    # query = "新聞とユダヤ人"
    limit = 5

    query = formQuery()
    request_url = base_url + f"{query}&limit={limit}"
    # print(request_url)

    try:
        response = requests.get("https://api.lib.harvard.edu/v2/items.json?title=Judaica&limit=1")
        response = requests.get(request_url)

        if response.status_code == 200: #success
            data = (json.loads(response.content))
            if data['items'] == None:
                print(f"NOT AT HARVARD")
                # print(data["identifier"][0]["@type"])
            #     extracted_data = extractOutput(data)
            #     # print(extracted_data[7])
            # elif held_at_harvard(extracted_data[7]):
            #     print(f"FOUND AT HARVARD")
            else:
                data = data["items"]["mods"]
                extracted_data = extractOutput(data)
                if held_at_harvard(extracted_data[7]):
                    print(f"FOUND AT HARVARD")
                else:
                    print(f"NOT AT HARVARD")
            # writeQueryResultToFile(data)
            
        else:
            print("error accessing API")
    except requests.exceptions.RequestException as e:
        print(response.status_code)
        # print(response.content)
        print(f"Error: {e}")

# data = data["items"]["mods"]
def extractOutput(data):
    isbn = data["identifier"]   # can be a list of id's
    english_title = ""
    original_title = ""
    author = ""
    translator = []
    publisher = ""
    pub_year = ""
    location = data["location"][0]["physicalLocation"]["#text"]               # will eventually check for Widener or Yenching

    extracted_output = [
        isbn, english_title, original_title, author, translator, publisher, pub_year, location
    ]
    return extracted_output

def held_at_harvard(extracted_output) -> bool:
    permanent = ["Havard Widener Library", "Harvard-Yenching Library"]
    # secondary checking mechanism
    # check for location (if Widener or Yenching --> True)
    at_harvard = False
    extracted_output = extracted_output.split(',')
    for library in extracted_output:
        if library in permanent:
            at_harvard = True
            return at_harvard
    return at_harvard

# helper function that writes json output to a testfile
def writeQueryResultToFile(data):
    formatted = json.dumps(data, indent=2)
    try:
        with open('/Users/jasonycwu/Desktop/HarvardScript/testOutput.txt', 'w+') as file:
            file.write(formatted)
    except:
        print(f"The file does not exist")

# takes input data (title, isbn, author name, publisher, publication year) and returns a formatted query for the API
def formQuery():
    # bookTitle = input("Enter book title: ")
    isbn = getISBN()
    # inputData = inputData()
    # isbn = inputData.getInput('testInput.txt')
    # isbn = getQueryFromFile()
    
    # author = input("Enter author name:")
    # publisher = input("Enter publisher:")
    # publishYear = input("Enter publication year:")
    # print(f"QUERY: {bookTitle} (ISBN: {isbn}) by {author} - published by {publisher} in {publishYear} ")
    isbn = isbn.replace("-", "")
    query = f"identifier={isbn}"
    return query

# get isbn query from user
def getISBN(input_stream=None):
    isbn_string = input("Enter ISBN:")
    isbn = isbn_string.replace("-", "")
    return isbn

def getQueryFromFile():
    inputData.getInput('testInput.txt')
    # with open('testInput.txt') as file:
    #     lines = file.readlines()
    #     lines = lines[1].split(',')
    #     isbn = lines[0]
    # return isbn
    return "0"

## runs the test functions
search_book_titles("test") 
# payload = QUERY.Payload()
# print(payload.title)
# formQuery()
