#! python

from datetime import date as dt
import time
import requests


def make_request():
    return requests.get("https://esi.evetech.net/latest/status/?datasource=tranquility")


def entry(response):
    game = "EVE Online"
    players = response.json()["players"]
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



