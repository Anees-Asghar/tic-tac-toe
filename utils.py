# importing libraries
import pandas as pd
import numpy as np


def generate_query_string(board):
	"""
	Generates a query string to query csv data satisfying the
	current state of the board.

	params:
		board: list

	returns:
		query_string: str

	"""
	query = []

	for i, let in enumerate(board):
		if not let == ' ':
			query.append(f"(df['V{str(i+1)}'] == '{let}')")

	query_string = "df[%s]" % (" & ".join(query))

	return query_string


def load_data():
	"""
	Loads csv data and modifies data for ease of use.
	Game result -> data['V10'] = {0, 1, 2}
		0 - x won
		1 - o won
		2 - Tie
	
	returns:
		df: pandas.core.frame.DataFrame
		Modified data frame.

	"""
	# load data
	print('Loading data... ', end="")
	df = pd.read_csv("data/tic-tac-toe-endgame.csv")
	print('Data loaded!')

	# set df['V10'] = 1 where x won
	# set df['V10'] = 0 where o won or tie
	df.replace('positive', 1, inplace=True)
	df.replace('negative', 0, inplace=True)

	return df