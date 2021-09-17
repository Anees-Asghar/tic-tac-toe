# tic-tac-toe
A python tic-tac-toe terminal based game against computer, without the use of minimax algorithm or hard coding.

---

## Motivation
I was interested in seeing how we can utilize the data of all possible tic-tac-toe games to produce an algorithm that can come up with educated responses to player moves. What I have implemented, therefore, is a tic-tac-toe game where the player, x,  always goes first. For the computer's turn, the algorithm goes through the game data to search for a move which has the highest probability of the game either ending in computer's favor or a tie, i.e., the player not winning.

## Setup
 - Clone this repo to your desktop.
 - cd to the root directory of this project and create and run a virtual enviornment (recommended).
 - Run `pip install -r requirements.txt` to install all the dependencies.

## Usage
From the root directory of this project run `python tic-tac-toe.py` on your terminal.
