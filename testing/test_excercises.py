import sys
from os.path import dirname as up
import unittest

dir = up(up(__file__))
sys.path.append(dir)
from utils.excercises import char_counter, episode_locations


class TestExcercises(unittest.TestCase):

    def test_char_counter_counter(self):
        """
        Checks the count of the characters in all resources, as well as the
        case insensitivity.
        """
        locations_names = [
            "Location", # 1
            "LLLlll", # 6
            "Nothing", # 0
            "Algo" # 1
        ] # Total = 8

        episodes_names_= [
            "Episoda", # 1
            "EEEeee", # 6
            "Apisoda", # 0
            "Apisode" # 1
        ] # Total = 8

        characters_names = [
            "Charavter", # 1
            "CCCccc", # 6
            "Varavter", # 0
            "Varacter" # 1
        ] # Total = 8

        results = char_counter(
            locations_names, 
            episodes_names_, 
            characters_names
        )

        self.assertEqual(results[0]["count"], 8)
        self.assertEqual(results[1]["count"], 8)
        self.assertEqual(results[2]["count"], 8)


if __name__ == '__main__':
    unittest.main()