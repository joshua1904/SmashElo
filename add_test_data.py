from sql import *
create_all_tables()
players_data = [
    ("Joshua", 1500),
    ("Marcel", 1600),
    ("Heiko", 1550)
]

fighters_data = [
    ("Game & Watch",),
    ("Bowser",),
    ("K K Rool",)
]

elos_data = [
    (1600, 1, 1),  # ELO of Fighter 1 for Player 1
    (1550, 2, 2),  # ELO of Fighter 2 for Player 2
    (1500, 3, 3)   # ELO of Fighter 3 for Player 3
]

games_data = [
    (1, 2, 1, 2, 3, 0),  # Player 1 with Fighter 1 wins against Player 2 with Fighter 2
    (2, 3, 2, 3, 2, 1),  # Player 2 with Fighter 2 wins against Player 3 with Fighter 3
    (3, 1, 3, 1, 3, 2)   # Player 3 with Fighter 3 wins against Player 1 with Fighter 1
]

# Insert sample players
for player in players_data:
    insert_player(player[0], player[1])

# Insert sample fighters
for fighter in fighters_data:
    insert_fighter(fighter[0])

# Insert sample ELOs
for elo in elos_data:
    insert_elo(elo[0], elo[1], elo[2])

# Insert sample games
for game in games_data:
    insert_game(game[0], game[1], game[2], game[3], game[4], game[5])