import requests
import json



def main():
    riotgames = "https://na1.api.riotgames.com/lol/"
    with open("backend/config.json", "r") as json_data_file:
        hehexd = json.load(json_data_file)
    apikey = "?api_key=" + hehexd['api_key']  


    summonerRequest = requests.get(riotgames + "summoner/v4/summoners/by-name/Shorthop" + apikey)
    summonerRequest = summonerRequest.json()
    accountId = summonerRequest["accountId"]
    encryptedId = summonerRequest["id"]
    matchHistory = requests.get(riotgames + "match/v4/matchlists/by-account/" + accountId + apikey)
    print (matchHistory.json())
    # r = requests.get(riotgames + "champion-mastery/v4/champion-masteries/by-summoner/" + encryptedId + apikey)
    # print(r.json())

main()