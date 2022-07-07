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

    def get_items(self):
        """
        Returns a list whose elements are the json objects that codify
        all the entities.
        """
        result = []
        response = requests.get(self.url + str([i for i in range(1, self.count + 1)])).json()
        for item in response:
            result.append(item)
        return result

    def get_names(self):
        """
        Returns a list whose elements are the names of all the entities.
        """
        result = []
        response = requests.get(self.url + str([i for i in range(1, self.count + 1)])).json()
        for item in response:
            result.append(item["name"])
        return result


"""
Reference: https://github.com/curiousrohan/ramapi
"""