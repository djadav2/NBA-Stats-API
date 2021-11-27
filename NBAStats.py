import requests
import json

def get_player_season_averages():
    player_year = input("Enter year: ")
    player_name = input("Enter name: ")
    print(player_name + "'s season averages: ")

    name_check = player_name.split(" ")
    if len(name_check) == 2:
        player_name = name_check[0] + "_" + name_check[1]
    
    player_string = "https://www.balldontlie.io/api/v1/players?search=" + player_name

    player = requests.get(player_string).content
    json_player = json.loads(player)
    player_id = json_player["data"][0]["id"]

    player_string2 = "https://www.balldontlie.io/api/v1/season_averages?season=" + player_year + "&player_ids[]=" + str(player_id)

    response = requests.get(player_string2).content
    json_response = json.loads(response)["data"][0]
    for key in json_response:
        print(key + ": " + str(json_response[key]))