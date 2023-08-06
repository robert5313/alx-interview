#!/usr/bin/python3

"""
You have n number of locked boxes.
Each numbered box from 0 to n - 1
"""


def canUnlockAll(boxes):
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for j in range(1, len(boxes) - 1):
        boxes_checked = False
        for x in range(len(boxes)):
            boxes_checked = j in boxes[x] and j != x
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
