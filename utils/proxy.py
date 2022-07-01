import requests

import yaml


with open("params.yaml", "r") as file:
    params = yaml.load(file, Loader=yaml.FullLoader)


"""
This entity manages the obtention of the desired data from the API.
"""

class Proxy:
    base_url = params["urls"]["base"]
    
    def __init__(self, url):
        self.url = self.base_url + url

        first_response = requests.get(self.url).json()
        self.count = first_response["info"]["count"]
        self.pages = first_response["info"]["pages"]
    
    def get_page(self, id):
        return requests.get(self.url + "?page=" + str(id)).json()

    def names(self):
        """
        Returns a generator whose elements are the names of the entities 
        found in every page.
        """
        for page in range(1, self.pages + 1):
            response = self.get_page(page)
            for item in response["results"]:
                yield item["name"]

    def items(self):
        """
        Returns a generator whose elements are the json objects that codify
        the entities found in every page.
        """
        for page in range(1, self.pages + 1):
            response = self.get_page(page)
            for item in response["results"]:
                yield item


"""
Reference: https://github.com/curiousrohan/ramapi
"""