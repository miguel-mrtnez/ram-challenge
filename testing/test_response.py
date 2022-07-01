import sys
from os.path import dirname as up
import json
import unittest

dir = up(up(__file__))
sys.path.append(dir)
from utils.response import ResponseManager


class TestResponseManager(unittest.TestCase):

    def test_type(self):
        """
        Checks the type of the response and its attributes.
        """
        result = ("Name", 25.691183499991894, [])
        response = ResponseManager([result])
        self.assertIsInstance(response.response, list)
        self.assertIsInstance(response.response[0], dict)
        self.assertIsInstance(response.response[0]["excercise_name"], str)
        self.assertIsInstance(response.response[0]["time"], float)
        self.assertIsInstance(response.response[0]["in_time"], bool)
        self.assertIsInstance(response.response[0]["results"], list)

    def test_is_json_serializable(self):
        """
        Checks if the response is JSON serializable.
        """
        result = ("Name", 25.691183499991894, [])
        response = ResponseManager([result])
        try:
            json.dumps(response.response)
            dump = True
        except TypeError:
            dump = False
        self.assertTrue(dump)


    def test_in_time_attr(self):
        """
        Checks the boolean assigned to the in_time attribute.
        """
        result_1 = ("Name 1", 2.0, [])
        result_2 = ("Name 2", 25.691183499991894, [])
        response_1 = ResponseManager([result_1])
        response_2 = ResponseManager([result_2])
        self.assertTrue(response_1.response[0]["in_time"])
        self.assertFalse(response_2.response[0]["in_time"])


if __name__ == '__main__':
    unittest.main()
