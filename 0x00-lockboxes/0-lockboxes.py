#!/usr/bin/python3

def canUnlockAll(boxes):
  """
  function that determines if all boxes can be opened secuencially 
  with keys contained in the other boxes 
  """
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

  print(box_opened, box_to_open)
  if len(box_to_open) == len(box_opened):
    return True
  else:
    return False