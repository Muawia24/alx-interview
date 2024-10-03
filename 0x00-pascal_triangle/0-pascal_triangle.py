#!/usr/bin/python3
""" 0-pascal_triangle.py """
def pascal_triangle(n):
    """
     returns a list of lists of integers representing
     the Pascal's triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1 for j in range(i)] for i in range(1, n + 1)]
    for row in range(2, len(triangle)):
        for column in range(1, len(triangle[row])):
            if column + 1 < len(triangle[row]):
                triangle[row][column] = triangle[row - 1][column - 1] + triangle[row - 1][column]

    return triangle

