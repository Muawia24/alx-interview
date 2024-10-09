#!/usr/bin/python3
""" 0. Lockboxes """
from collections import deque

""" BFS function """


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
    Write a method that determines if all the boxes can
    be opened.
    """
    try:
        i = 0
        keys = []

        q = deque()

        visited = [False] * len(boxes)
        visited[i] = True

        q.append(i)

        while (q):
            curr = q.popleft()
            keys.append(curr)

            for x in boxes[curr]:
                if not visited[x]:
                    visited[x] = True
                    q.append(x)
        if len(keys) == len(boxes):
            return True

        return False
    except IndexError:
        return False
