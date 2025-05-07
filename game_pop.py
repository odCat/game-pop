#!/usr/bin/env python3

import datetime
import requests


def make_request():
    api_url = "https://esi.evetech.net/latest/status/?datasource=tranquility"
    return requests.get(api_url).json()


def entry(response):
    game = "EVE Online"
    players = response["players"]
    date_and_time = datetime.datetime.now(datetime.UTC)
    date = date_and_time.date().isoformat()
    hour = date_and_time.hour

    return {
            "game": game,
            "players": players,
            "date": date,
            "hour": hour
        }


if __name__ == "__main__":
    print(entry(make_request()))



