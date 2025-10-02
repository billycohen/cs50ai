"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board) -> str:
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    return X if x_count == o_count else O


def actions(board) -> set:
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board: list, action: tuple) -> list[list]:
    """
    Returns the board that results from making move (i, j) on the board.
    """
    try:
        board_copy = copy.deepcopy(board)
        current_player = player(board_copy)
        (i, j) = action
        if board_copy[i][j] != EMPTY:
            raise Exception(f"{(i, j)} is not a valid move!")

        board_copy[i][j] = current_player
        return board_copy
    except Exception:
        print(f"Exception raised during result..: {board, action}")


def winner(board) -> str | None:
    rows = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
    ]

    columns = [
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
    ]

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for line in rows + columns + diagonals:
        for player in [X, O]:
            if all(board[i][j] == player for (i, j) in line):
                return player

    return None


def terminal(board) -> bool:
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    if not any(cell == EMPTY for row in board for cell in row):
        return True

    return False


def utility(board) -> int:
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    score = 0

    potential_winner = winner(board)

    if potential_winner == X:
        score = 1
    elif potential_winner == O:
        score = -1

    return score


def min_value(board) -> int:
    v = math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

        if v == -1:
            break

    return v


def max_value(board) -> int:
    v = -math.inf
    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

        if v == 1:
            break

    return v


def minimax(board) -> tuple:
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)

    current_player = player(board)
    available_actions = actions(board)
    best_move = tuple()

    if current_player == X:
        v = -math.inf
        for action in available_actions:
            pv = min_value(result(board, action))

            if pv > v:
                v = pv
                best_move = action

    else:
        v = math.inf
        for action in available_actions:
            pv = max_value(result(board, action))

            if pv < v:
                v = pv
                best_move = action

    return best_move
