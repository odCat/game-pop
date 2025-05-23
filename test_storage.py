#!/usr/bin/env python3

import os
import pytest

import game_pop as gp
import storage


class TestStorage:

    TEST_DB_FILE = "test_game_statistics.db"

    @pytest.fixture(scope="class", autouse=True)
    def db_connection(self):
        db = storage.Storage(self.TEST_DB_FILE)

        yield db

        db.connection.close()
        os.remove(self.TEST_DB_FILE)

    @pytest.fixture(autouse=True)
    def create_population_table(self, db_connection):
        db_connection.create_population_table("test_population")

        yield

        db_connection.cursor.execute('''DROP TABLE IF EXISTS test_population''')

    def test_cannot_insert_duplicates(self, db_connection):
        response = {
            'players': 29896,
            'server_version': '2889100',
            'start_time': '2025-05-03T11:01:08Z'
        }
        db_connection.insert_into_population(gp.entry(response), "test_population")
        db_connection.insert_into_population(gp.entry(response), "test_population")

        query = "SELECT COUNT(*) FROM test_population"
        actual = db_connection.cursor.execute(query).fetchone()[0]
        expected = 1

        assert expected == actual


if __name__ == '__main__':
    pytest.main()
