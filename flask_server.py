from flask import Flask, render_template, request, flash
from utils import *
import sqlite3
from sql import insert_player

app = Flask(__name__)
app.secret_key = "key"


@app.route('/')
def player_ranking():
    try:
        player_data = get_ranked_players()
        return render_template("player_ranking.html", players=player_data)
    except sqlite3.Error:
        return render_template("player_ranking.html", players=[])


@app.route('/fighter_ranking')
def fighter_ranking():
    try:
        fighters_data = get_ranked_fighters()
        return render_template("fighter_ranking.html", fighters=fighters_data)
    except sqlite3.Error:
        return render_template("fighter_ranking.html", fighters=[])


@app.route('/add')
def add_game_template():
    try:
        fighters = [i[0] for i in get_fighters()]
        players = [i[0] for i in get_players()]
        return render_template("add.html", fighters=fighters, players=players)
    except sqlite3.Error:
        return render_template("fighter_ranking.html", fighters=[])


@app.route("/submit_game", methods=["POST"])
def add_game_request():
    try:
        fighters = [i[0] for i in get_fighters()]
        players = [i[0] for i in get_players()]
        winner_player = request.form.get("winner_player")
        winner_fighter = request.form.get("winner_character")
        loser_player = request.form.get("loser_player")
        loser_fighter = request.form.get("loser_character")
        winner_kills = request.form.get("winner_kills")
        loser_kills = request.form.get("loser_kills")
        if not (winner_kills.isnumeric() or loser_kills.isnumeric()):
            flash("Kill values have to be a number", "error")
            return render_template("add.html", fighters=fighters, players=players)
        winner_kills = int(winner_kills)
        loser_kills = int(loser_kills)
        add_game(winner_player, winner_fighter, loser_player, loser_fighter, winner_kills, loser_kills)
        flash("Successfully added game!", "success")
        return render_template("add.html", fighters=fighters, players=players)
    except sqlite3.Error:
        return render_template("fighter_ranking.html", fighters=[])


@app.route("/add_player", methods=["POST"])
def add_player():
    try:
        fighters = [i[0] for i in get_fighters()]
        players = [i[0] for i in get_players()]
        player = request.form.get("player_name")
        if player in players:
            flash("Player already in Database!", "error")
            return render_template("add.html", fighters=fighters, players=players)
        if player == "":
            flash("Player Name cant be empty", "error")
            return render_template("add.html", fighters=fighters, players=players)
        insert_player(player, START_ELO)
        flash("Successfully added Player", "success")
        return render_template("add.html", fighters=fighters, players=players)
    except sqlite3.Error:
        flash("Something went wrong, Sorry!", "error")
        return render_template("fighter_ranking.html", fighters=[])


@app.route('/games')
def games():
    try:
        games = get_all_games()
        return render_template("games.html", games=games)
    except sqlite3.Error:
        return render_template("fighter_ranking.html", fighters=[])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
