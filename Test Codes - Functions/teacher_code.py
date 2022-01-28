def flip(items):
  flipped = []
  for i in range(1,len(items)+1):
    flipped += [items[-i]]
  return flipped