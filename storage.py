#!/usr/bin/env python3

import sqlite3

import game_pop as gp


class Storage:

    def __init__(self, db_file="game_population.db"):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def create_population_table(self, table="population"):
        query = f'''
            CREATE TABLE IF NOT EXISTS {table} (
                game TEXT NOT NULL,
                date TEXT NOT NULL,
                hour INTEGER NOT NULL,
                players INTEGER NOT NULL
            );
        '''
        self.cursor.execute(query)
        self.connection.commit()

    def is_entry_present(self, entry):
        query = f'''
            SELECT COUNT(*)
            FROM {entry["table"]}
            WHERE game = :game
                AND date = :date
                AND hour = :hour
            ;
        '''
        result = self.cursor.execute(query, entry).fetchall()[0][0] > 0
        self.connection.commit()
        return result

    def insert(self, entry, table="population"):
        self.create_population_table(table)
        entry["table"] = table

        is_present = self.is_entry_present(entry)
        if is_present > 0:
            return False

        query = f"INSERT INTO {entry['table']} VALUES (:game, :date, :hour, :players);"
        self.cursor.execute(query, entry)
        self.connection.commit()
        return True


if __name__ == '__main__':
    storage = Storage()
    response = {
        'players': 29896,
        'server_version': '2889100',
        'start_time': '2025-05-03T11:01:08Z'
    }
    storage.insert(gp.entry(response))
    print(storage.cursor.execute('''SELECT * FROM population;''').fetchall())