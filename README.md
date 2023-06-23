## Harvard Library Lookup Automation Script
Drafted by Jason Woo

## Purpose
The goal of this script is to be able to automate the process of checking
whether a title is being held within the Harvard Library system. Users should
be able to input a single title -- along with author's name, ISBN, year of
publication, publisher, and pagenation -- or a list of titles.

## Implementation
The script uses Harvard LibraryCloud API to access Harvard University Library's
bibliographic metatdata. The logic is as follows:

    user input  -> Input 
                -> Payload   
                -> Query    -> [Harvard LibraryCloud]   -> Data       
                                                        -> Determinant 
                                                        -> Output -> output data
                                                    
## Modules
main driver code - creates instances of the classes below and interact

class Input - handles csv, txt file or a single input. The module should parse
the input and extract relevant data to put in Payload for query searches. These 
fields include:
    ISBN, book title, author, translator, publisher, and publish year.
    ISBN, author, and translator should be either lists or dictionaries since
    there might be more than one.

class Payload - a dataclass that holds the relevant data fields required for a
search in the Harvard Library database. Payload includes ISBN, book title, 
author, translator, publisher, and publish year.

class Query - a formatted string representing the request url being sent to the
Harvard LibraryCloud API. Include fields from Payload. 

class Data - representing the response received from the Harvard LibraryCloud
API. The class should parse data received from the API and keep the relevant
fields for Determinant.
    A book not found in Harvard Library's database will have empty fields

class Determinant - logic class that handles the determination of whether a
given title is being held at Harvard's permanent collection. 
    Should Data be empty, the output of the Determinant will be false

class Output - handles output/modification to files. Users should be able to
specific where (path) they would like to store their outputs. 
    If their input was a csv file, their output should also be a correspoding
    csv file.