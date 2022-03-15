import core.code_sim as codeSimarity
import core.sca as sca
import numpy as np
from rich import print

def test1():

  fileLocations = [
    "./test_codes/friday/part2_q1/model.py",
    "./test_codes/friday/part2_q1/student1.py",
    "./test_codes/friday/part2_q1/student2.py"
  ]

  code = sca.scaTools(fileLocations[0])
  modelCode = [code.longCode]

  studentCodes = []
  for i in range(1,len(fileLocations)):
    code = sca.scaTools(fileLocations[i])
    studentCodes += [code.longCode]


  print("\nShowing code similarity results...\n")
  # [modelCode, studentCodes[0], studentCodes[1]]
  results = codeSimarity.detect(
        modelCode + studentCodes, 
        diff_method=codeSimarity.TreeDiff, 
        # diff_method=pycode_similar.UnifiedDiff,
        keep_prints=True, 
        module_level=False
    )
  for i in range(len(results)):
    print(f"\nResult for Student{i+1}\n")
    print(results[i])



if __name__ == '__main__':
  test1()