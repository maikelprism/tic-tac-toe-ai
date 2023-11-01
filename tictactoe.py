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
    # return [[O, O, EMPTY],
    #         [X, EMPTY, EMPTY],
    #         [X, X, EMPTY]]

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    o_counter = 0

    for row in board:
        for tile in row:
            if tile == X:
                x_counter += 1
            elif tile == O:
                o_counter += 1
    
    if x_counter == o_counter:
        return X
    else:
        return O
                

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)
    result_board[action[0]][action[1]] = player(board)

    return result_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontal
    for row in board:
        if row[0] == row[1] == row[2] == X:
            return X
        if row[0] == row[1] == row[2] == O:
            return O
    
    # Check vertical
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        if board[0][i] == board[1][i] == board[2][i] == O:
            return O
        
    # Check diagonal
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O:
        return O
    
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][2] == board[1][1] == board[2][0] == O:
        return O
    
    return None


def terminal(board):
    
    # Check for winner
    if winner(board) != None:
        return True
    
    else:
        # Check for tie
        for row in board:
            for tile in row:
                if tile == EMPTY:
                    return False
        
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)

    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    isMaximizing = True if player(board) == X else False

    print(isMaximizing)

    if isMaximizing:
        return maximize(board, -math.inf, math.inf)[1]
    else:
        return minimize(board, -math.inf, math.inf)[1]

def maximize(board, alpha, beta):

    best_move = (-math.inf, None)
    possible_actions = actions(board)
    for i in range(len(possible_actions)):
        resulting_board = result(board, possible_actions[i])
        if terminal(resulting_board):
            if utility(resulting_board) > best_move[0]:
                best_move = (utility(resulting_board), possible_actions[i])
        else:
            minimize_move = minimize(resulting_board, alpha, beta)
            if minimize_move[0] > best_move[0]:
                best_move = (minimize_move[0], possible_actions[i])
        alpha = max(best_move[0], alpha)
        if beta <= alpha:
            break

    return best_move

def minimize(board, alpha, beta):

    best_move = (math.inf, None)
    possible_actions = actions(board)
    for i in range(len(possible_actions)):
        resulting_board = result(board, possible_actions[i])
        if terminal(resulting_board):
            if utility(resulting_board) < best_move[0]:
                best_move = (utility(resulting_board), possible_actions[i])
        else:
            maximize_move = maximize(resulting_board, alpha, beta)
            if maximize_move[0] < best_move[0]:
                best_move = (maximize_move[0], possible_actions[i])
        beta = min(best_move[0], beta)
        if beta <= alpha:
            break

    return best_move
        


