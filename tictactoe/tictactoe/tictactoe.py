"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count moves for each player
    x_count = 0
    o_count = 0

    for i, j, cell in get_cells(board):
        if cell == X:
            x_count += 1
        elif cell == O:
            o_count += 1

    if x_count > o_count:
        return O
    else:
        return X
    
    return X

def actions(board):
    return {(i, j) for i, j, cell in get_cells(board) if cell == EMPTY}


def result(board, action):
    i= action[0]
    j= action[1]
    if board[i][j] != EMPTY:
        raise ValueError("Invalid action")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
   if winner(board) is not None or all(cell != EMPTY for row in board for cell in row):
       return True
   else:
       return False
 
def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    if actions(board) == []:
        return None
    if player(board) == X:
        v = -math.inf
        best_action = None
        for action in actions(board):
            action_value = min_value(result(board, action))
            if action_value > v:
                v = action_value
                best_action = action
        return best_action
    else:
        v = math.inf
        best_action = None
        for action in actions(board):
            action_value = max_value(result(board, action))
            if action_value < v:
                v = action_value
                best_action = action
        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def get_cells(board):
    for i in range(3):
        for j in range(3):
            yield (i, j, board[i][j])
