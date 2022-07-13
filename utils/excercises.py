
def char_counter(locations_names, episodes_names, characters_names):

    l_counter = e_counter = c_counter = 0

    for location in locations_names:
        location = location.lower()
        l_counter += location.count("l")

    for episode in episodes_names:
        episode = episode.lower()
        e_counter += episode.count("e")

    for character in characters_names:
        character = character.lower()
        c_counter += character.count("c")

    results = [
        {
            "char": "l",
            "count": l_counter,
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

def episode_locations(episodes, characters):

    dict_episodes = dict()
    
    for i in episodes:
        dict_episodes[i["id"]] = {
            "name": i["name"],
            "episode": i["episode"],
            "locations": set()
        }

    for char in characters:
        for ep in char["episode"]:
            dict_episodes[int(ep[40:])]["locations"].add(char["origin"]["name"])

    for ep in dict_episodes.values():
        ep["locations"] = list(ep["locations"])

    return list(dict_episodes.values())