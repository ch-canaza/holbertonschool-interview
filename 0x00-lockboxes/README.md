# 0x00-lockboxes

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False

### secuence:  
> box zero is open, we test every key in its corresponding box
if we find a box with no keys and we do not have more keys, it is over
if a key is in iŧs own box, it is also over
so we count how many boxes could be opened

### execute as
> ./main_0.py