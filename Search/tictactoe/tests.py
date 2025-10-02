import unittest

import tictactoe as ttt

X = "X"
O = "O"
EMPTY = None


class TestTicTacToe(unittest.TestCase):
    def test_player(self) -> None:
        self.assertEqual(
            ttt.player(
                [[EMPTY, EMPTY, EMPTY], [X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
            ),
            O,
        )

        self.assertEqual(
            ttt.player([[EMPTY, EMPTY, X], [O, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]),
            X,
        )

    def test_actions(self) -> None:
        self.assertEqual(
            ttt.actions(
                [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
            ),
            {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)},
        )

        self.assertEqual(
            ttt.actions([[X, X, X], [O, O, O], [X, O, X]]),
            set(),
        )

    def test_result(self) -> None:
        self.assertEqual(
            ttt.result(
                [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]],
                (0, 0),
            ),
            [[X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]],
        )

        self.assertEqual(
            ttt.result(
                [[X, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]],
                (1, 1),
            ),
            [[X, EMPTY, EMPTY], [EMPTY, O, EMPTY], [EMPTY, EMPTY, EMPTY]],
        )

        with self.assertRaises(Exception) as error:
            (
                ttt.result(
                    [[X, X, O], [X, O, O], [O, X, X]],
                    (1, 1),
                ),
            )

        self.assertEqual(str(error.exception), "(1, 1) is not a valid move!")

    def test_winner(self) -> None:
        x_wins1 = [
            [X, X, X],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
        ]
        x_wins2 = [
            [X, EMPTY, EMPTY],
            [X, EMPTY, EMPTY],
            [X, EMPTY, EMPTY],
        ]
        x_wins3 = [
            [X, EMPTY, EMPTY],
            [EMPTY, X, EMPTY],
            [EMPTY, EMPTY, X],
        ]
        self.assertEqual(ttt.winner(board=x_wins1), X)
        self.assertEqual(ttt.winner(board=x_wins2), X)
        self.assertEqual(ttt.winner(board=x_wins3), X)

        o_wins1 = [
            [O, O, O],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
        ]
        o_wins2 = [
            [O, EMPTY, EMPTY],
            [O, EMPTY, EMPTY],
            [O, EMPTY, EMPTY],
        ]
        o_wins3 = [
            [O, EMPTY, EMPTY],
            [EMPTY, O, EMPTY],
            [EMPTY, EMPTY, O],
        ]
        self.assertEqual(ttt.winner(board=o_wins1), O)
        self.assertEqual(ttt.winner(board=o_wins2), O)
        self.assertEqual(ttt.winner(board=o_wins3), O)

        nobody_wins = [
            [X, X, O],
            [O, O, X],
            [X, X, O],
        ]

        self.assertEqual(ttt.winner(board=nobody_wins), None)

    def test_terminal(self) -> None:
        x_wins1 = [
            [X, X, X],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
        ]
        self.assertEqual(ttt.terminal(board=x_wins1), True)

        o_wins1 = [
            [O, O, O],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
        ]

        self.assertEqual(ttt.terminal(board=o_wins1), True)

        nobody_wins = [
            [X, X, O],
            [O, O, X],
            [X, X, O],
        ]

        self.assertEqual(ttt.terminal(board=nobody_wins), True)

        remaining_move = [
            [X, X, O],
            [O, EMPTY, X],
            [X, X, O],
        ]

        self.assertEqual(ttt.terminal(board=remaining_move), False)
