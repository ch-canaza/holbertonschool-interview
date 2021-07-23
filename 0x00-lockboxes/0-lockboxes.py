#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    function that determines if all boxes can be opened secuencially
    with keys contained in the other boxes
    """
    if type(boxes) is not list or not all(type(box) is list for box in boxes):
        return False
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    if not boxes[0] and len(boxes) > 1:
        return False
    box_to_open = list(range(1, len(boxes)))
    box_opened = []
    for box in boxes:
        if box == []:
            break
        for key in box:
            if key in box_to_open and key not in box_opened:
                if boxes.index(box) == key:
                    break
                else:
                    box_opened.append(key)

    if len(box_to_open) == len(box_opened):
        return True
    else:
        return False
