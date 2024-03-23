import sqlite3

from sql import *
from table_classes import *
from calculate_elo import update_ratings

START_ELO = 1500

def _get_player_data(player_data: tuple | None) -> Player | None:
    if player_data is not None:
        return Player(*player_data)
    return None


def _get_fighter_data(fighter_data: tuple | None) -> Fighter | None:
    if fighter_data is not None:
        return Fighter(*fighter_data)
    return None


def _add_fighter_elo(player: Player, fighter_name: str) -> Fighter | None:
    """Inserts a new elo for a players fighter. Returns fighter to get the new Id
    If the fighter dosent exist -> return None"""
    if not (fighter := get_fighter_by_name(fighter_name)):
        return None
    insert_elo(START_ELO, fighter[0], player.name)
    return _get_fighter_data(get_data_of_player_fighter(player.name, fighter[0]))


def add_game(winner_name: str, winner_fighter_name: str, loser_name: str, loser_fighter_name: str, winner_stock: int,
             loser_stock: int):
    # get player data from database
    winner_player = _get_player_data(get_data_of_player(winner_name))
    loser_player = _get_player_data(get_data_of_player(loser_name))
    winner_fighter = _get_fighter_data(get_data_of_player_fighter(winner_name, winner_fighter_name))
    if not winner_fighter:
        winner_fighter = _add_fighter_elo(winner_player, winner_fighter_name)
    loser_fighter = _get_fighter_data(get_data_of_player_fighter(loser_name, loser_fighter_name))
    if not loser_fighter:
        loser_fighter = _add_fighter_elo(loser_player, loser_fighter_name)
    if not _no_arguments_are_none(winner_fighter, loser_fighter, winner_player, loser_player):
        return False
    # calculate new elos
    new_winner_elo = update_ratings(winner_player.elo, loser_player.elo, True)
    new_loser_elo = update_ratings(loser_player.elo, winner_player.elo, False)
    new_winner_fighter_elo = update_ratings(winner_fighter.elo, loser_fighter.elo, True)
    new_loser_fighter_elo = update_ratings(loser_fighter.elo, winner_fighter.elo, False)
    # insert new elos and game in database
    try:
        insert_game(winner_player.name, loser_player.name, winner_fighter.name, loser_fighter.name, winner_stock, loser_stock)
        update_elo_of_player(winner_name, new_winner_elo)
        update_elo_of_player(loser_name, new_loser_elo)
        update_elo_of_player_fighter(winner_fighter.name, winner_player.name, new_winner_fighter_elo)
        update_elo_of_player_fighter(loser_fighter.name, loser_player.name, new_loser_fighter_elo)
    except sqlite3.Error:
        return False
    return True

def get_ranked_players() -> list[dict]:
    return [dataclasses.asdict(Player(*i)) for i in get_all_elos_of_players()]

def get_ranked_fighters() -> list[dict]:
    return [dataclasses.asdict(EloOfPlayerFighter(*i)) for i in get_all_elos_of_fighters()]

def get_all_games() -> list[dict]:
    return [dataclasses.asdict(Games(*i)) for i in get_games()]


def _no_arguments_are_none(*args):
    return None not in args


if __name__ == "__main__":
    print(add_game("Heiko", "Bowser", "Joshua", "Bowser",3, 2))
    # print(get_ranked_fighters())
    print(get_games())
