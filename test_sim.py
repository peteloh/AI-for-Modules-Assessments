import pycode_similar

MODEL_CODE_STRING = """
def flip(items):
  flipped = []
  for i in range(1,len(items)+1):
    flipped += [items[-i]]
  return flipped
"""

STUDENT_CODE_STRING = [
# STUDENT CODE 0 = Full Mark Code - Exact same as model code
"""
def flip(items):
  flipped = []
  for i in range(1,len(items)+1):
    flipped += [items[-i]]
  return flipped
""",
# STUDENT CODE 1 = Full mark code, exact same structure, different variable
"""
def flip(items):
  flipped_items = []
  for i in range(1,len(items)+1):
    flipped_items += [items[-i]]
  return flipped_items
""",
# STUDENT CODE 2 = Should be full mark but written using alternative of +=
"""
def flip(items):
  flipped_items = []
  for i in range(1,len(items)+1):
    flipped_items = flipped_items + [items[-i]]
  return flipped_items
""",
# STUDENT CODE 3 = Should be full mark but written using while loop instead of for loop
"""
def flip(items):
  flipped_items = []
  i = 1
  while i < len(items)+1:
    flipped_items = flipped_items + [items[-i]]
    i += 1
  return flipped_items
""",
# STUDENT CODE 4 = Correct Code but return syntax error at the end
"""
def flip(items):
  flipped = []
  for i in range(1,len(items)+1):
    flipped += [items[-i]]
  return flippedd
""",
# STUDENT CODE 5 = Completely Wrong Code (Can compile)
"""
def flip(items):
  flipped = ['random stuff']
  return flipped
""",
# STUDENT CODE 6 = Completely Wrong Code (Just return, cant even compile)
"""
def flip(items):
  return flip
""",
# STUDENT CODE 7 = Not even a function
"""
hello
"""]

for i in range(len(STUDENT_CODE_STRING)):
    result = pycode_similar.detect(
        [MODEL_CODE_STRING, STUDENT_CODE_STRING[i]], 
        diff_method=pycode_similar.TreeDiff, 
        # diff_method=pycode_similar.UnifiedDiff,
        keep_prints=False, 
        module_level=False
    )
    print(f"Student Code {i} result = " + str(round(result[0][1][0].plagiarism_percent,3)))