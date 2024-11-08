#!/usr/bin/python3
"""
0. N queens
"""


import sys
from typing import List


def backtrack(
        n: int, i: int,
        col: List,
        pos_diagonal: List,
        neg_diagonal: List,
        board: List) -> None:
    """
    Backtracking method for possitioning the non-attacking
    Queens.
    """
    if i == n:
        queens = []
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == 1:
                    queens.append([x, y])
        print(queens)
        return

    if i < n:
        for j in range(n):
            if (j not in col and i + j not in pos_diagonal
                    and i - j not in neg_diagonal):
                col.append(j)
                pos_diagonal.append(i + j)
                neg_diagonal.append(i - j)
                board[i][j] = 1
                backtrack(n, i + 1, col, pos_diagonal, neg_diagonal, board)

                col.pop()
                pos_diagonal.pop()
                neg_diagonal.pop()
                board[i][j] = 0


def queen(n: int) -> None:
    """
    The N queens puzzle is the challenge of placing N
    non-attacking queens on an NxN chessboard. A
    program that solves the N queens problem.
    """
    board = [[0] * n for i in range(n)]

    backtrack(n, 0, [], [], [], board)


if __name__ == "__main__":

    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(args[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        queen(n)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
