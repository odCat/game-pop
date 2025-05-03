#!python

from datetime import date as dt
import requests
import time


def make_request():
    api_url = "https://esi.evetech.net/latest/status/?datasource=tranquility"
    return requests.get(api_url).json()


def entry(response):
    game = "EVE Online"
    players = response["players"]
    date = dt.today().isoformat()
    hour = time.strftime("%H", time.localtime())

    return {
            "game": game,
            "players": players,
            "date": date,
            "hour": hour
        }


if __name__ == "__main__":
    print(entry(make_request()))



