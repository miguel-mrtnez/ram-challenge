from utils.proxy import Proxy


def char_counter(locations_url, episodes_url, characters_url):

    locations = Proxy(locations_url)
    episodes = Proxy(episodes_url)
    characters = Proxy(characters_url)

    i_counter = e_counter = c_counter = 0

    for location in locations.names():
        i_counter += location.count("l") + location.count("L")

    for episode in episodes.names():
        e_counter += episode.count("e") + episode.count("E")

    for character in characters.names():
        c_counter += character.count("c") + character.count("C")

    results = [
        {
            "char": "l",
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

def episode_locations(episodes_url, characters_url):
    episodes = Proxy(episodes_url)
    characters = Proxy(characters_url)

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