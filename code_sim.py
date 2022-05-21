# basic imports
import numpy as np
from rich import print

# import forked core codes
import core.pycode_similar_fork.pycode_similar.pycode_similar as pycode_similar
from core.scoss_fork.scoss import Scoss

# import other core codes
import core.sca as sca

def pycode_similar_analysis(modelCodeDir : str, studentCodesDir : list):

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

def scoss_analysis(modelCodeDir : str, studentCodesDir : list):
  sc = Scoss(lang='py')
  sc.add_metric('count_operator', threshold=0) 
  sc.add_metric('set_operator', threshold=0)
  sc.add_metric('hash_operator', threshold=0)

  sc.add_file(modelCodeDir)
  for directory in studentCodesDir:
    sc.add_file(directory)

  sc.run()
  print(sc.get_matches(and_thresholds=True))


def main():
  exercise = "ExA"
  modelCodeDir = f"./data/Markscheme/{exercise}_solution.py"
  
  # we are using 2 to 30 to train, 31 to 40 to test
  start = 2
  end = 30
  studentCodesDir = []
  for i in range(start,end+1):
    studentCodesDir += [f"./data/{exercise}/C{i}_{exercise}.py"]

  print(studentCodesDir)
  # testPycodeSimilar(modelCodeDir, studentCodesDir)
  # testScoss(modelCodeDir, studentCodesDir)
  
  # result = getSimilarity(modelCodeDir, studentCodesDir)
  # print(result)

if __name__ == '__main__':
  main()