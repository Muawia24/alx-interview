#!/usr/bin/python3
"""
0. Change comes from within
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
     Determines the fewest number of coins needed to
     meet a given amount total.
    """
    if total <= 0 or not coins:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    if dp[total] == float('inf'):
        return -1

    return dp[total]
