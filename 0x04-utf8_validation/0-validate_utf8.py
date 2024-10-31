#!/usr/bin/python3
"""
 UTF-8 Validation
"""


def check(arr):
    """
    Check for continuation bytes
    """
    for x in arr:
        b = format(x, "08b")
        if b[:2] != "10":
            return False
    return True


def validUTF8(data):
    """
    Validates UTF-8 characters
    """
    for i in range(len(data)):
        if isinstance(data[i], int) and data[i] > 244 or data[i] < 0:
            return False
        b = format(data[i], "08b")
        if b[0] == 0:
            continue
        if b[:3] == "110":
            if i >= (len(data) - 1):
                return False
            if not check(list((data[i + 1],))):
                return False
            continue

        if b[:4] == "1110":
            if i >= (len(data) - 2):
                return False
            if not check(list((data[i + 1], data[i + 2]))):
                return False
            continue

        if b[:5] == "11110":

            if i >= (len(data) - 3):
                return false
            if not check(list((data[i + 1], data[i + 2], data[i + 3]))):
                return False
            continue

        return True
