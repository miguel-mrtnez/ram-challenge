import json


"""
This entity manages the creation of the desired response 
in JSON format.
"""

class ResponseManager:
    def __init__(self, excercises):
        self.excercises = excercises
        self.output_path = "output.json"
        self.make(excercises)

    def make(self, excercises):
        self.response = []
        for excercise in excercises:
            dict = {
                "excercise_name": excercise[0],
                "time": excercise[1],
                "in_time": True if excercise[1] < 3 else False,
                "results": excercise[2]
            }
            self.response.append(dict)

    def dump(self):
        with open(self.output_path, 'w') as output_file:
            json.dump(self.response, output_file, indent=4)