CREATE_STATEMENT_PLAYERS = """CREATE TABLE IF NOT EXISTS players (
    name VARCHAR(255) PRIMARY KEY,
    elo INT
);
"""

CREATE_STATEMENT_FIGHTERS = """CREATE TABLE IF NOT EXISTS fighters (
    name VARCHAR(255) PRIMARY KEY
);"""

CREATE_STATEMENT_ELOS = """CREATE TABLE IF NOT EXISTS elos (
    id INTEGER PRIMARY KEY,
    value INT,
    fighter_name INT,
    player_name INT,
    FOREIGN KEY (fighter_name) REFERENCES fighters(name),
    FOREIGN KEY (player_name) REFERENCES players(name)
);"""

CREATE_STATEMENT_GAMES = """CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    winner_player_name varchar(255),
    loser_player_name varchar(255),
    winner_fighter_name varchar(255),
    loser_fighter_name varchar(255),
    winner_stocks INT,
    loser_stocks INT,
    FOREIGN KEY (winner_player_name) REFERENCES players(name),
    FOREIGN KEY (loser_player_name) REFERENCES players(name),
    FOREIGN KEY (winner_fighter_name) REFERENCES fighters(name),
    FOREIGN KEY (loser_fighter_name) REFERENCES fighters(name)
);"""

UPDATE_PLAYER = "UPDATE players SET name = ?, elo = ? WHERE name = ?"
INSERT_PLAYER_STATEMENT = """INSERT INTO players (name, elo) VALUES (?, ?)"""
DELETE_PLAYER = """DELETE FROM player WHERE name = ?"""

INSERT_FIGHTER_STATEMENT = "INSERT INTO fighters (name) VALUES (?)"
DELETE_FIGHTER = "DELETE FROM fighters WHERE name = ?"

UPDATE_ELO = "UPDATE elos SET value = ?, fighter_name = ?, player_name = ? WHERE name = ?"
INSERT_ELO_STATEMENT = "INSERT INTO elos (value, fighter_name, player_name) VALUES (?, ?, ?)"
DELETE_ELO = "DELETE FROM elos WHERE id = ?"


INSERT_GAME_STATEMENT = "INSERT INTO games (winner_player_name, loser_player_name, winner_fighter_name, loser_fighter_name, winner_stocks, loser_stocks) VALUES (?, ?, ?, ?, ?, ?)"
DELETE_GAME = "DELETE FROM games WHERE id = ?"

GET_ALL_GAMES_STATEMENT = """Select winner_player_name as winner, loser_player_name as loser, winner_fighter_name as winners_fighter, loser_fighter_name as losers_fighter, winner_stocks, loser_stocks from games
	ORDER BY games.id DESC"""

GET_ALL_PLAYERS_RANKED = """select * from players ORDER BY elo DESC;"""

GET_DATA_OF_PLAYER = "SELECT * from players Where name = ?;"
UPDATE_ELO_OF_PLAYER = "UPDATE players Set elo = ? Where name = ?;"
UPDATE_ELO_OF_PLAYER_FIGHTER = "UPDATE elos Set value = ? Where player_name = ? AND fighter_name = ?"
GET_DATA_OF_PLAYER_FIGHTER = """Select fighter_name, value from elos
    Where player_name = ? And fighter_name = ?"""

GET_FIGHTER_BY_NAME = "Select * from fighters Where name = ?"

GET_ALL_FIGHTERS_RANKED = """Select player_name, fighter_name, value FROM elos
    ORDER BY elos.value Desc"""

GET_PLAYER_NAMES = """Select name from players Order by name"""
GET_FIGHTER_NAMES = """Select name from fighters Order by name """
