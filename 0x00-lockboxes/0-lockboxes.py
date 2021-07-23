#!/usr/bin/python3


def canUnlockAll(boxes):
    """canUnlockAll function to check if
    boxes unlock or not
    Args:
        boxes (list): list of boxes (list)
    Return: False if all boxes cannot unlock and True otherwise
    """
    if type(boxes) is not list or not all(type(box) is list for box in boxes):
        return False
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    if not boxes[0] and len(boxes) > 1:
        return False
    unlock = {k: False for k in range(len(boxes))}
    unlock[0] = True
    keys = [key for key in boxes[0]]
    while keys:
        new_k = []
        for key in keys:
            if key in unlock.keys() and unlock[key] is False:
                new_k += boxes[key]
                unlock[key] = True
        if all(unlock.values()) and len(unlock) == len(boxes):
            return True
        keys = new_k
    return False
    