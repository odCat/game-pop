import pytest

import game_pop as gp


def test_game_pop():
    response = {
         'players': 29896,
         'server_version': '2889100',
         'start_time': '2025-05-03T11:01:08Z'
    }
    entry = gp.entry(response)

    assert "game" in entry
    assert "players" in entry
    assert "date" in entry
    assert "hour" in entry


if __name__ == '__main__':
    pytest.main()