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
    i = 0
    while i < len(data):
        if not isinstance(data[i], int) or data[i] > 244 or data[i] < 0:
            return False
        if data[i] in [192, 193]:
            return False

        b = format(data[i], "08b")
        if b[0] == "0":
            i += 1
            continue

        elif b[:3] == "110":
            if i + 1 >= len(data) or not check([data[i + 1]]):
                return False
            i += 2

        elif b[:4] == "1110":
            if i + 2 >= len(data) or not check([data[i + 1], data[i + 2]]):
                return False
            i += 3

        elif b[:5] == "11110":
            if i + 3 >= len(data) or not check(
                    [data[i + 1], data[i + 2], data[i + 3]]):
                return False
            i += 4
        else:
            return False

    return True
