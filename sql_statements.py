CREATE_STATEMENT_PLAYERS = """CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    elo INT
);
"""

CREATE_STATEMENT_FIGHTERS = """CREATE TABLE IF NOT EXISTS fighters (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255)
);"""

CREATE_STATEMENT_ELOS = """CREATE TABLE IF NOT EXISTS elos (
    id INTEGER PRIMARY KEY,
    value INT,
    fighter_id INT,
    player_id INT,
    FOREIGN KEY (fighter_id) REFERENCES fighters(id),
    FOREIGN KEY (player_id) REFERENCES players(id)
);"""

CREATE_STATEMENT_GAMES = """CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    winner_player_id INT,
    loser_player_id INT,
    winner_fighter_id INT,
    loser_fighter_id INT,
    winner_stocks INT,
    loser_stocks INT,
    FOREIGN KEY (winner_player_id) REFERENCES players(id),
    FOREIGN KEY (loser_player_id) REFERENCES players(id),
    FOREIGN KEY (winner_fighter_id) REFERENCES fighters(id),
    FOREIGN KEY (loser_fighter_id) REFERENCES fighters(id)
);"""

UPDATE_PLAYER = "UPDATE players SET name = ?, elo = ? WHERE id = ?"
INSERT_PLAYER_STATEMENT = """INSERT INTO players (name, elo) VALUES (?, ?)"""
DELETE_PLAYER = """DELETE FROM player WHERE id = ?"""

UPDATE_FIGHTER = "UPDATE fighters SET name = ? WHERE id = ?"
INSERT_FIGHTER_STATEMENT = "INSERT INTO fighters (name) VALUES (?)"
DELETE_FIGHTER = "DELETE FROM fighters WHERE id = ?"

UPDATE_ELO = "UPDATE elos SET value = ?, fighter_id = ?, player_id = ? WHERE id = ?"
INSERT_ELO_STATEMENT = "INSERT INTO elos (value, fighter_id, player_id) VALUES (?, ?, ?)"
DELETE_ELO = "DELETE FROM elos WHERE id = ?"

UPDATE_GAME = "UPDATE games SET winner_player_id = ?, loser_player_id = ?, winner_fighter_id = ?, loser_fighter_id = ?, winner_stocks = ?, loser_stocks = ? WHERE id = ?"
INSERT_GAME_STATEMENT = "INSERT INTO games (winner_player_id, loser_player_id, winner_fighter_id, loser_fighter_id, winner_stocks, loser_stocks) VALUES (?, ?, ?, ?, ?, ?)"
DELETE_GAME = "DELETE FROM games WHERE id = ?"

GET_ALL_GAMES_STATEMENT = """Select winning_player.name as winner, loser_player.name as loser, winning_fighter.name as winners_fighter, loser_fighter.name as losers_fighter, games.winner_stocks, games.loser_stocks from games
    Inner Join players winning_player On winning_player.id = games.winner_player_id
    Inner Join players loser_player On loser_player.id = games.loser_player_id
	Inner Join fighters winning_fighter On winning_fighter.id = games.winner_fighter_id
	Inner Join fighters loser_fighter On loser_fighter.id = games.loser_fighter_id
	ORDER BY games.id DESC"""

GET_ALL_PLAYERS_RANKED = """select * from players ORDER BY elo DESC;"""

GET_DATA_OF_PLAYER = "SELECT * from players Where name = ?;"
UPDATE_ELO_OF_PLAYER = "UPDATE players Set elo = ? Where name = ?;"
UPDATE_ELO_OF_PLAYER_FIGHTER = "UPDATE elos Set value = ? Where player_id = ? AND fighter_id = ?"
GET_DATA_OF_PLAYER_FIGHTER = """Select fighters.id, fighters.name, elos.value from elos
    Inner join players On players.id = elos.player_id
    Inner Join fighters ON fighters.id = elos.fighter_id
    Where players.name = ? And fighters.name = ?"""

GET_FIGHTER_BY_NAME = "Select * from fighters Where name = ?"

GET_ALL_FIGHTERS_RANKED = """Select players.name, fighters.name, elos.value FROM elos
    INNER JOIN players ON players.id = elos.player_id
    INNER JOIN fighters ON fighters.id = elos.fighter_id
    ORDER BY elos.value Desc"""

GET_PLAYER_NAMES = """Select name from players Order by name"""
GET_FIGHTER_NAMES = """Select name from fighters Order by name """
