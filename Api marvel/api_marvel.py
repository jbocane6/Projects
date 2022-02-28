#!/usr/bin/python3
from fileinput import close
import requests
import json
from keys import values


# First, we get the dictionary that contains the keys and hash
valor = values()
# Head is the main part of the url
head = "https://gateway.marvel.com:443/v1/public/"
# Next we're gonna use f instead format to control amount of characters
keys = f"ts={valor['ts']}&apikey={valor['public_key']}&hash={valor['hash']}"
url = "{}events?{}".format(head, keys)

result = requests.get(url)
if result.status_code == 200:
    # First we get the text obtained, and store the results
    results = json.loads(result.text)["data"]["results"]
    output_list = []
    for i in range(10 if len(results) >= 10 else len(results)):
        # Recover the values we need, store them
        id = results[i]["id"]
        title = results[i]["title"]
        description = results[i]["description"]
        start = results[i]["start"]
        end = results[i]["end"]
        # There are several creators, we're gonna concatenate and store them
        creators = ", ".join(creator["name"] for creator in results[i][
            "creators"]["items"])
        # Create an dictionary with the values stored
        dic = {"ID": id, "Title": title, "Description": description,
               "Start": start, "End": end, "Creators": creators}
        # Add the dictionary to the list
        output_list.append(dic)
    with open('data.json', 'w') as file:
        # Create, add values and format the json
        json.dump(output_list, file, indent=4)
        close
