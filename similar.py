# basic imports
import numpy as np
from rich import print

# import forked core codes
import core.pycode_similar_fork.pycode_similar.pycode_similar as pycode_similar
from core.scoss_fork.scoss import Scoss

# import other core codes
import core.sca as sca

def getSimilarity(modelCodeDir : str, studentCodesDir : list):

  inputCodes = [
    # modelCode,
    # student1,
    # student2, 
    # etc.
  ]

  modelCode = sca.scaTools(modelCodeDir)

  studentFileNames = []

  if modelCode.isFunction == False:
    inputCodes += [modelCode.convertToFunction()]

    for i in range(len(studentCodesDir)):
      code = sca.scaTools(studentCodesDir[i])
      inputCodes += [code.convertToFunction()]
      studentFileNames += [code.filename]
  
  else:
    # is already a function
    inputCodes += [modelCode.longCode]

    for i in range(len(studentCodesDir)):
      code = sca.scaTools(studentCodesDir[i])
      inputCodes += [code.longCode]
      studentFileNames += [code.filename]
  
  print("\nShowing code similarity results...\n")
  # [modelCode, studentCodes[0], studentCodes[1]]
  unifiedDiffResults = pycode_similar.detect(
        inputCodes, 
        diff_method=pycode_similar.UnifiedDiff, 
        keep_prints=True, 
        module_level=False
    )

  treeDiffResults = pycode_similar.detect(
      inputCodes, 
      diff_method=pycode_similar.TreeDiff, 
      keep_prints=True, 
      module_level=False
  )

  results = {
    "unifiedDiff": {},
    "treeDiff": {}
  }

  for i in range(len(unifiedDiffResults)):

    print(f"UnifiedDiff Result for Student File {i+1}: {unifiedDiffResults[i][1][0].plagiarism_percent}")
    print(f"TreeDiff    Result for Student File {i+1}: {treeDiffResults[i][1][0].plagiarism_percent}\n")

    results["unifiedDiff"][studentFileNames[i]] = unifiedDiffResults[i][1][0].plagiarism_percent
    results["treeDiff"][studentFileNames[i]] = treeDiffResults[i][1][0].plagiarism_percent
    
  return results


def testPycodeSimilar(modelCodeDir : str, studentCodesDir : list):
  print(f"\nTesting codesim1...\n")

  code = sca.scaTools(modelCodeDir)
  modelCode = [code.longCode]

  studentCodes = []
  for i in range(len(studentCodesDir)):
    code = sca.scaTools(studentCodesDir[i])
    studentCodes += [code.longCode]

  print("\nShowing code similarity results...\n")
  # [modelCode, studentCodes[0], studentCodes[1]]
  unifiedDiffResults = pycode_similar.detect(
        modelCode + studentCodes, 
        diff_method=pycode_similar.UnifiedDiff, 
        keep_prints=True, 
        module_level=False
    )

  treeDiffResults = pycode_similar.detect(
      modelCode + studentCodes, 
      diff_method=pycode_similar.TreeDiff, 
      keep_prints=True, 
      module_level=False
  )
  
  for i in range(len(unifiedDiffResults)):
    print(f"UnifiedDiff Result for Student{i+1}: {unifiedDiffResults[i][1][0].plagiarism_percent}")
    print(f"TreeDiff    Result for Student{i+1}: {treeDiffResults[i][1][0].plagiarism_percent}\n")
  
  print(f"\nTest Completed!\n")

def testScoss(modelCodeDir : str, studentCodesDir : list):
  sc = Scoss(lang='py')
  sc.add_metric('count_operator', threshold=0) 
  sc.add_metric('set_operator', threshold=0)
  sc.add_metric('hash_operator', threshold=0)

  sc.add_file(modelCodeDir)
  for directory in studentCodesDir:
    sc.add_file(directory)

  sc.run()
  print(sc.get_matches(and_thresholds=True))

def test():
  modelCodeDir = "./test_codes/friday/part2_q1/model.py"
  studentCodesDir = [
    "./test_codes/friday/part2_q1/student1.py",
    "./test_codes/friday/part2_q1/student2.py",
    "./test_codes/friday/part2_q1/student3.py",
    "./test_codes/friday/part2_q1/student4.py"
    ]
  # testPycodeSimilar(modelCodeDir, studentCodesDir)
  # testScoss(modelCodeDir, studentCodesDir)
  
  result = getSimilarity(modelCodeDir, studentCodesDir)
  print(result)


if __name__ == '__main__':
  test()