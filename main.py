import yaml

from utils.excercises import char_counter, episode_locations
from utils.response import ResponseManager
from utils.proxy import Proxy
from utils.timer import Timer


# Load the parameters from the yaml file
with open("params.yaml", "r") as file:
    params = yaml.load(file, Loader=yaml.FullLoader)

locations_url = params["urls"]["locations"]
episodes_url = params["urls"]["episodes"]
characters_url = params["urls"]["characters"]


# Instantiate timers
timer_cc = Timer()
timer_el = Timer()


# Char counter excecution
timer_cc.start()

locations = Proxy(locations_url)
episodes = Proxy(episodes_url)
characters = Proxy(characters_url)

results_cc = char_counter(locations.names, episodes.names, characters.names)
timer_cc.stop()
response_cc = ("Char counter", timer_cc.get_time(), results_cc)


# Episode locations excecution
timer_el.start()
results_el = episode_locations(episodes.items, characters.items)
timer_el.stop()
response_el = ("Episode locations", timer_el.get_time(), results_el)


# Response generation
response = ResponseManager([response_cc, response_el])
response.dump()