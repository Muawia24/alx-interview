#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid) -> int:
    """
    Args:
        grid: is a list of list of integers:
                0 represents water.
                1 represents land.
    Return:
         returns the perimeter of the island described in
         grid.
    """
    if not grid:
        return 0

    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perimeter += 4

                if row - 1 >= 0 and grid[row - 1][col] == 1:
                    perimeter -= 1
                if row + 1 < len(grid) and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                    perimeter -= 1
                if col - 1 >= 0 and grid[row][col - 1] == 1:
                    perimeter -= 1

    return perimeter
