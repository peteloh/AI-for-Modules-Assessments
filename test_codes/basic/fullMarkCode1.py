def flip(items):
  flipped_items = []
  for i in range(1,len(items)+1):
    flipped_items += [items[-i]]
  return flipped_items