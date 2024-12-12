#!/usr/bin/python3
""" 0. Prime Game"""


def SieveOfEratosthenes(n):
    """
    Args:
        n: range of prime
    Return:
        list of prim numbers in range n
    """

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p]):
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            prime[p] = p
    # Print all prime numbers
    return [n for n in prime if type(n) == int]


def isWinner(x, nums):
    """
    Maria and Ben are playing a game. Given a set of
    consecutive integers starting from 1 up to and
    including n, they take turns choosing a prime number
    from the set and removing that number and its
    multiples from the set. The player that cannot make
    a move loses the game.

    Args:
        x: number of rountds
        nums:  is an array of n
    Return:
        name of the player that won the most rounds
    """

    points = {'Maria': 0, 'Ben': 0}
    for num in nums:
        win = SieveOfEratosthenes(num)
        if len(win) % 2 != 0:
            points['Maria'] += 1
        else:
            points['Ben'] += 1

    winner = max(zip(points.values(), points.keys()))[1]

    return winner
