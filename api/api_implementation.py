'''
Implements the query and parsing methods for each API using the interface class from interface.py

'''

import requests
from api import interface
import api.keys as keys

'''
        Info parsed in order of index location:
        0: Uploader ID from original website
        1: Uploader name 
        2: Full size image
        3: Large size image 
        4: Small size image 
        5: Link to original URL image was pulled from
        6: which API the image was pulled from
'''

# Implements API interface methods for Pexel
class Pexel(interface.ApiParserInterface):
    # Sends a search request to Pexel 
    def send_query(self: object, query: str, page: int, per_page: int) -> list:
        # Please utilize your own Pexel API key. 
        if keys.PEXEL_KEY == '':
            raise Exception("Invalid key: Pexel key cannot be empty.")

        url = "https://api.pexels.com/v1/search"
        headers = {'Authorization': keys.PEXEL_KEY}
        payload = {'query': query, 'page': page, 'per_page': per_page}
        request = []
        request = requests.get(url, headers=headers, params=payload)

        # Check if key was authorized
        if request.status_code == 401:
            raise Exception("Invalid key: Pexel key unauthorized. Status code 401.")

        return request.json()

    # Parses the necessary information from the returned json file 
    def parse(self: object, info: list) -> list:
        parse_info = []
        for x in info['photos']:
            parse_info.append([x['id'], x['photographer'], x['src']['original'], x['src']['large2x'], x['src']['medium'], x['url'], "Pexel"])
        return parse_info
    

# Implements API interface methods for Unsplash
class Unsplash(interface.ApiParserInterface):
    # Sends a search request to Unsplash 
    def send_query(self: object, query: str, page: int, per_page: int) -> list:
        # Please utilize your own Unsplash API key. 
        if keys.UNSPLASH_KEY == '':
            raise Exception("Invalid key: Unsplash key cannot be empty.")
        
        url = "https://api.unsplash.com/search/photos"      
        headers = {'Authorization': "Client-ID " + keys.UNSPLASH_KEY}
        payload = {'query': query, 'page': page, 'per_page': per_page}
        request = []
        request = requests.get(url, headers=headers, params=payload)

        # Check if key was authorized
        if request.status_code == 401:
            raise Exception("Invalid key: Unsplash key unauthorized. Status code 401.")

        return request.json()

    # Parses the necessary information from the returned json file 
    def parse(self: object, info: list) -> list:
        parse_info = []
        for x in info['results']:
            parse_info.append([x['id'], x['user']['username'], x['urls']['raw'], x['urls']['full'], x['urls']['regular'], x['links']['html'], "Unsplash"])
        return parse_info

