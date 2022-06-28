import yaml
import requests


with open("params.yaml", "r") as file:
    params = yaml.load(file, Loader=yaml.FullLoader)

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
        for page in range(1, self.pages + 1):
            response = self.get_page(page)
            for item in response["results"]:
                yield item["name"]


if __name__ == "__main__":
    locations = Proxy(params["urls"]["locations"])
    print("Count: ", locations.count)
    print("Pages", locations.pages)
    
    counter = 0
    for name in locations.names():
        print(name)
        counter += 1

    print("Total: ", counter)

    