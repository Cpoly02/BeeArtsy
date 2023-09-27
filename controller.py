'''
    Queries the APIs based on user input and manipulates the returned information before returning it to the user. 
'''

from api import api_implementation as api
from random import randrange
import numpy as np

# Constants - index locations in results array
ID = 0          # Uploader ID
OGUSER = 1      # Uploader name
IMG_RAW = 2     # Full size image
IMG_LRG = 3     # Large size image
IMG_SM = 4      # Small size image
ORIGIN_URL = 5  # Link to original API page image was pulled from
ORIGIN = 6      # which API the image was pulled from

# Variables 
results = []            # Contains parsed data returned from APIs
sessionID = 0           # Keep track of session ID for session storage 

# user inputted variables 
search = ""             # User inputted search query
quantity = ""           # How many images per page are retrieved 
interval = ""           # How long to display each image. 
max_page_num = ""       # Max page to retrieve from 


###################################################
#               API and Data Manip                #
################################################### 

# Function that queries APIS, parses necessary information, and returns single array of combined elements
def requestAPIs(query, page = 1, per_page = 15):
    apis = []
    apis.append(api.Pexels())
    apis.append(api.Unsplash())

    results = []
    for a in apis: 
        for r in a.parse(a.send_query(query, page, per_page)):
            results.append(r) 
    
    return results


###################################################
#                       Web App                   #
###################################################

# Handles requests to the API and returns the results in a parsed array 
def Handler(search, quantity, max_page_num):
    print(search)  # Print result query to terminal

    # Randrange errors out if range is (1,1) 
    if max_page_num == 1: 
        p = 1; 
    else: 
        p = randrange(1, max_page_num)  # get random page number from range 1 - N. N is a user-entered value

    global results
    results = []
    results = requestAPIs(search, p, quantity*2)  # API call 

    # If no results were returned because the page number was too high (APIs didn't have that many images of the requested subject)
    # try again 
    if len(results) == 0 and p > 1:
       results = requestAPIs(search, 1, quantity*2)  # API call 

    np.random.shuffle(results)    # Shuffle results for more varied results 

    results = results[:int(quantity)]
    return results
