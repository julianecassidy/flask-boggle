from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game
    print(game_id)
    board = game.board

    return jsonify({"gameId": game_id, "board": board})

@app.post("/api/score-word")
def score_word():
    """Checks if word is valid word on board"""
    word = request.json
    print(word)

    # Check if word
    # Check if on board
    # Check if valid word
