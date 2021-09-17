# importing libraries
import os
import time
from utils import load_data, generate_query_string


def make_move(board, pos, let):
	"""
	Makes a move by changing the value of the square 
	picked on the board to x or o.

	params:
		board: list
		pos: int
		let: str {'o', 'x'}

	"""
	board[pos] = let


def print_board(board):
	"""
	Prints out the board according to the template provided.

	params:
		board: list

	"""
	print('		 %s | %s | %s ' % (board[0], board[1], board[2]))
	print('		-----------')
	print('		 %s | %s | %s ' % (board[3], board[4], board[5]))
	print('		-----------')
	print('		 %s | %s | %s ' % (board[6], board[7], board[8]))


def is_available(board, pos):
	"""
	Checks if the position on the board is available.

	params:
		board: list
		pos: int

	returns:
		is_available: bool

	"""
	is_available = board[pos] == ' '
	return is_available


def is_winner(board, let):
	"""
	Checks if the player using letter 'let' has won.
	
	params:
		board: list
		let: str {'o', 'x'}

	returns:
		is_winner: bool

	"""
	is_winner = (board[0] == let and board[1] == let and board[2] == let) or \
		(board[3] == let and board[4] == let and board[5] == let) or\
		(board[6] == let and board[7] == let and board[8] == let) or\
		(board[0] == let and board[3] == let and board[6] == let) or\
		(board[1] == let and board[4] == let and board[7] == let) or\
		(board[2] == let and board[5] == let and board[8] == let) or\
		(board[0] == let and board[4] == let and board[8] == let) or\
		(board[2] == let and board[4] == let and board[6] == let)

	return is_winner


def find_best_move(board):
	"""
	Finds the best move for the computer.

	params:
		board: list

	return:
		best_move: int
		Index of the best move to make for comp.

	"""
	best_move = None

	# find all available moves
	possible_moves = [i for i, let in enumerate(board) if let == ' ']

	# return if no moves available
	if not len(possible_moves):
		return best_move

	# the probality of a positive result for each of the possible moves
	# positive result constitutes games tied and games won by o
	probs = []

	# calculate positive result probability for each available move
	for move in possible_moves:
		# make that move on a temporary board
		tmp_board = board[:]
		make_move(tmp_board, move, 'o')

		# query the data for all entries that satisfy the current
		# state of the board (matches) and then query matches for
		# games that end on a positive result for o (pos_matches)
		matches = eval(generate_query_string(tmp_board))
		pos_matches = matches.loc[matches['V10'] == 0]

		# count for each query
		matches_count = matches.shape[0]
		pos_matches_count = pos_matches.shape[0]

		# append the probabily of positive result for this move
		probs.append(pos_matches_count / matches_count)

	# find and return the move with the highest positive result
	# probability
	max_probs = max(probs)
	max_probs_index = probs.index(max_probs)
	best_move = possible_moves[max_probs_index]
	return best_move


def main():
	"""
	Runs the game.

	"""
	# welcome message
	print('------------------------------')
	print("  Welcome to Tic Tac Toe!")
	print('------------------------------')

	# initialize and print board
	board = [' ' for i in range(9)]
	print_board(board)
	
	# back and forth moves for player and comp
	while True:
		# player move (until a valid move is provided)
		while True:
			try:
				# get player move
				print('\n')
				player_move = int(input('Enter a position (1-9): ')) - 1
				print('\n')

				# check if within range
				if 0 <= player_move <= 8:
					# check if square available
					if is_available(board, player_move):
						break
					else:
						print(f'Position {player_move+1} is already filled.\n')
				else:
					print('Please enter a number within range 1-9.\n')
			
			except: # if the value provided is not int
				print('Please insert a number.\n')

		make_move(board, player_move, 'x')
		print('Your move: ')
		print_board(board)

		# check if player won
		if is_winner(board, 'x'):
			print('------------------------------')
			print('  You won. Good job!')
			print('------------------------------')
			return

		# only for the experience
		time.sleep(1)

		# computer move
		comp_move = find_best_move(board)
		if comp_move == None: # if board is full
			print('------------------------------')
			print('  Game tied. Well played!')
			print('------------------------------')
			return
		make_move(board, comp_move, 'o')
		print('Comp move: ')
		print_board(board)

		# check if comp won
		if is_winner(board, 'o'):
			print('------------------------------')
			print('  Comp won. Good game!')
			print('------------------------------')
			return


if __name__ == "__main__":
	# assert that the dataset file exists
	ROOT_DIR = os.path.abspath(os.getcwd())
	assert os.path.exists(os.path.join(ROOT_DIR, "data", "tic-tac-toe-endgame.csv")), \
	"Could not find the tic-tac-toe-endgame.csv file."
	
	# load tic-tac-toe data
	df = load_data()

	# run the game
	main()