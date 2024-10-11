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
        # keys list
        keys = []

        # Create a queue for BFS
        q = deque()

        # Initially mark all the vertices as not visited
        # When we push a vertex into the q, we mark it as
        # visited
        visited = [False] * len(boxes)

        # Mark the source node as visited and enqueue it
        visited[i] = True

        q.append(i)

        # Iterate over the queu
        while (q):

            # Dequeue a vertex from queue and add it to list
            curr = q.popleft()
            keys.append(curr)

            # Get all adjacent vertices of the dequeued
            # vertex. If an adjacent has not been visited,
            # mark it visited and enqueue it
            if not isinstance(boxes[curr], list):
                return False

            for x in boxes[curr]:
                if x >= len(boxes):
                    continue

                if not visited[x]:
                    visited[x] = True
                    q.append(x)

        if len(keys) == len(boxes):
            return True

        return False
    except IndexError:
        return False
