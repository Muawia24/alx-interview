#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Args:
        matrix: list of lists
    Return:
        Nothing

    Given an n x n 2D matrix, rotate it 90 degrees
    clockwise.The matrix is edited in-place.
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        matrix[i].reverse()
