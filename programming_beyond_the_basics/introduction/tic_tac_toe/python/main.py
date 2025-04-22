'''
now:
* variable to hold board state
* play_game, that starts game
    current_player = 'X'
    displays board
    prompts for input position of current player (position)
                print enter position for current_player, results [1....9]
    checks if position is occpied
        if occupied, throw error
        if not, assign that to that poistion
    determine end state
        if X or O print X or O as winner
        if is_game_completed
                print draw
                stop the program
    current_player = toggled_player
    repeat

* play_game, starts the game

X is_game_completed  (board)
    check if all the box are filled, results [True, False]
X toggle (player)
        if X return 0, if O returns X
X determine_winner (board)
    picks up the winner, results in [X, O, None]
X is_occupied (row, col)
    returns if a position is occupied or not, results in [true, false]
X display_board (board)
    visualized the board
X position_translator (position)
    return row col
X determine_end_state

X prompter (player)
    prompts to enter postion, validate_position, and asks till they enter valid position

later:
     * unit tests
     * refactor determine_end_state
     * refactor display_board
     * work on math for position_translator
     * good var names
'''

import sys


def toggle_player(player):
    return 'X' if player == 'O' else 'O'


def display_board(board):
    for row in board:
        modified_row = list(map(lambda box: box if box else ' ', row))
        print('|', end='')
        print('|'.join(modified_row), end='')
        print('|')


def is_game_completed(board):
    for row in board:
        for box in row:
            if not box:
                return False
    return True


def is_occupied(row, col, board):
    return board[row][col] != None


def determine_winner(board):
    cols = [[(x, y) for x in range(0, 3)] for y in range(0, 3)]  # tech debt
    rows = [[(x, y) for y in range(0, 3)] for x in range(0, 3)]
    diagnals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

    def find_unique_in_line(line):
        unique = set(board[x][y] for x, y in line)
        if len(unique) == 1 and 'X' in unique:
            return 'X'
        if len(unique) == 1 and 'O' in unique:
            return 'O'
        return None

    for line in [*rows, *cols, *diagnals]:
        winner = find_unique_in_line(line)
        if winner:
            return winner
    return None


def position_translator(position):
    position_to_row_col_mapping = {1: (0, 0),
                                   2: (0, 1),
                                   3:  (0, 2),
                                   4: (1, 0),
                                   5: (1, 1),
                                   6: (1, 2),
                                   7: (2, 0),
                                   8: (2, 1),
                                   9: (2, 2)
                                   }
    return position_to_row_col_mapping[position]


def validate_position(position):
    if 1 <= position <= 9:
        return True
    return False


def prompt(player):
    while True:
        try:
            position = input(f"Enter position for {player} -> ")
            position = int(position)
            is_valid_positon = validate_position(position)
            if (is_valid_positon):
                return position
        except ValueError:
            print("Not a valid postion, try again")


def determine_end_state(board):
    winner = determine_winner(board)
    if winner:
        print(f"Winner {winner}")
        sys.exit(0)
    if is_game_completed(board):
        print('Draw')
        sys.exit(0)
    return False


def print_game_instruction():

    print("Tic Tac Toe")
    print("When promted enter the position from 1 to 9")
    print("Positon mapping of the board is given below")
    display_board([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])


def play_game():
    # states
    current_player = 'X'
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]

    print_game_instruction()

    while True:
        print('current board')
        display_board(board)

        position = prompt(current_player)
        row, col = position_translator(position)
        occupied = is_occupied(row, col, board)

        if (occupied):
            print('The positon is occupied, try different positon')
            continue

        board[row][col] = current_player
        determine_end_state(board)
        current_player = toggle_player(current_player)


play_game()
