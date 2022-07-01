import yaml

from utils.proxy import Proxy


with open("params.yaml", "r") as file:
    params = yaml.load(file, Loader=yaml.FullLoader)


def char_counter():

    locations = Proxy(params["urls"]["locations"])
    episodes = Proxy(params["urls"]["episodes"])
    characters = Proxy(params["urls"]["characters"])

    i_counter = 0
    e_counter = 0
    c_counter = 0

    for location in locations.names():
        i_counter += location.count("l")
        i_counter += location.count("L")

    for episode in episodes.names():
        e_counter += episode.count("e")
        e_counter += episode.count("E")

    for character in characters.names():
        c_counter += character.count("c")
        c_counter += character.count("C")

    results = [
        {
            "char": "i",
            "count": i_counter,
            "resource": "location"
        },
        {
            "char": "e",
            "count": e_counter,
            "resource": "episode"
        },
        {
            "char": "c",
            "count": c_counter,
            "resource": "character"
        }
    ]
    return results

def episode_locations():
    episodes = Proxy(params["urls"]["episodes"])
    characters = Proxy(params["urls"]["characters"])

    dict_episodes = dict()
    
    for i in episodes.items():
        dict_episodes[i["id"]] = {
            "name": i["name"],
            "episode": i["episode"],
            "locations": set()
        }

    for char in characters.items():
        for ep in char["episode"]:
            dict_episodes[int(ep[40:])]["locations"].add(char["origin"]["name"])

    for ep in dict_episodes.values():
        ep["locations"] = list(ep["locations"])

    return list(dict_episodes.values())