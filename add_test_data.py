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

fighters = [
    "Mario", "Donkey Kong", "Link", "Samus", "Dark Samus", "Yoshi", "Kirby", "Fox",
    "Pikachu", "Luigi", "Ness", "Captain Falcon", "Jigglypuff", "Peach", "Daisy",
    "Bowser", "Ice Climbers", "Sheik", "Zelda", "Dr. Mario", "Pichu", "Falco",
    "Marth", "Lucina", "Young Link", "Ganondorf", "Mewtwo", "Roy", "Chrom", "Mr. Game & Watch",
    "Meta Knight", "Pit", "Dark Pit", "Zero Suit Samus", "Wario", "Snake", "Ike",
    "Squirtle", "Ivysaur", "Charizard", "Diddy Kong", "Lucas", "Sonic", "King Dedede",
    "Olimar", "Lucario", "R.O.B.", "Toon Link", "Wolf", "Villager", "Mega Man",
    "Wii Fit Trainer", "Rosalina & Luma", "Little Mac", "Greninja", "Mii Brawler",
    "Mii Swordfighter", "Mii Gunner", "Palutena", "Pac-Man", "Robin", "Shulk",
    "Bowser Jr.", "Duck Hunt", "Ryu", "Ken", "Cloud", "Corrin", "Bayonetta",
    "Inkling", "Ridley", "Simon", "Richter", "King K. Rool", "Isabelle", "Incineroar",
    "Piranha Plant", "Joker", "Hero", "Banjo & Kazooie", "Terry", "Byleth", "Min Min",
    "Steve", "Sephiroth", "Pyra", "Mythra", "Kazuya", "Sora"
]

# Insert all fighters into the database
for fighter in fighters:
    insert_fighter(fighter)