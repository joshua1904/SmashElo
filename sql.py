import sqlite3
from sql_statements import *

DATABASE_FILE = 'your_database.db'


def create_players_table():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_STATEMENT_PLAYERS)


def create_fighters_table():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_STATEMENT_FIGHTERS)


def create_elos_table():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_STATEMENT_ELOS)


def create_games_table():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_STATEMENT_GAMES)


# Create all tables
def create_all_tables():
    create_players_table()
    create_fighters_table()
    create_elos_table()
    create_games_table()


# Update a player in the players table
def update_player(player_id: int, name: str, elo: int):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE_PLAYER, (name, elo, player_id))
        conn.commit()


# Insert a new player into the players table
def insert_player(name: str, elo: int):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_PLAYER_STATEMENT, (name, elo))
        conn.commit()


# Delete a player from the players table
def delete_player(player_id: int):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE_PLAYER, (player_id,))
        conn.commit()


# Update a fighter in the fighters table

# Insert a new fighter into the fighters table
def insert_fighter(name: str):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_FIGHTER_STATEMENT, (name,))
        conn.commit()


# Delete a fighter from the fighters table
def delete_fighter(fighter_id: int):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE_FIGHTER, (fighter_id,))
        conn.commit()


# Update an elo record in the elos table
def update_elo(elo_id: int, value: int, fighter_id: int, player_id: int):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE_ELO, (value, fighter_id, player_id, elo_id))
        conn.commit()


# Insert a new elo record into the elos table
def insert_elo(value: int, fighter_name: str, player_name: str):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_ELO_STATEMENT, (value, fighter_name, player_name))
        conn.commit()


# Delete an elo record from the elos table
def delete_elo(elo_id: int):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE_ELO, (elo_id,))
        conn.commit()


# Insert a new game record into the games table
def insert_game(winner_player_name: str, loser_player_name: str, winner_fighter_name: str, loser_fighter_name: int,
                winner_stocks: int, loser_stocks: int):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(INSERT_GAME_STATEMENT, (
            winner_player_name, loser_player_name, winner_fighter_name, loser_fighter_name, winner_stocks,
            loser_stocks))
        conn.commit()


# Delete a game record from the games table
def delete_game(game_id: int):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE_GAME, (game_id,))
        conn.commit()


def get_id_and_elo_of_player(player_name: str):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        return cursor.execute(GET_DATA_OF_PLAYER, (player_name,)).fetchone()


def get_data_of_player(fighter_name: str):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        return cursor.execute(GET_DATA_OF_PLAYER, (fighter_name,)).fetchone()


def get_data_of_player_fighter(player_name: str, fighter_name: str):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        return cursor.execute(GET_DATA_OF_PLAYER_FIGHTER, (player_name, fighter_name)).fetchone()


def update_elo_of_player(player_name: str, elo: int):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE_ELO_OF_PLAYER, (elo, player_name))
        conn.commit()


def update_elo_of_player_fighter(fighter_name: str, player_name: str, elo: int):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(UPDATE_ELO_OF_PLAYER_FIGHTER, (elo, player_name, fighter_name))
        conn.commit()


def get_fighter_by_name(name: str) -> tuple:
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        return cursor.execute(GET_FIGHTER_BY_NAME, (name,)).fetchone()


def get_all_elos_of_fighters():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        return cursor.execute(GET_ALL_FIGHTERS_RANKED).fetchall()


def get_all_elos_of_players():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        return cursor.execute(GET_ALL_PLAYERS_RANKED).fetchall()


def get_players():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        return cursor.execute(GET_PLAYER_NAMES).fetchall()


def get_fighters():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        return cursor.execute(GET_FIGHTER_NAMES).fetchall()


def get_games():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        return cursor.execute(GET_ALL_GAMES_STATEMENT).fetchall()


def get_last_game():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        return cursor.execute(GET_LAST_GAME_STATEMENT).fetchone()

def delete_last_game():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(DELETE_LAST_GAME_STATEMENT)
        conn.commit()