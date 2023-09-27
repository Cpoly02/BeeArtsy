''' API interface to query and parse information from API '''

class ApiParserInterface:
    def send_query(self: object, query: str, page: int, per_page: int) -> list:
        '''Send a request to the api using the search query inputted as parameter'''
        pass

    def parse(self: object, info: list) -> list:
        '''Parse desired information from json parameter and place into returning list. Return in the format [[id, original_uploader, image_url,...], [...], [...]]'''
        pass

