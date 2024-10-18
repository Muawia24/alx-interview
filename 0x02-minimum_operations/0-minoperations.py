#!/usr/bin/python3
""" 0-minoperations.py """
from typing import List, Callable


def fact(n: int, factors: List[int]) -> int:
    """ Returns the sum of the prime factors of n """
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
            return fact(int(n / i), factors)
    factors.append(n)
    return sum(factors)


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if not isinstance(n, int) or n <= 1:
        return 0
    factors = []
    return fact(n, factors)
