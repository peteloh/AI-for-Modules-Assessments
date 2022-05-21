# basic imports
import numpy as np
from rich import print

# import other core codes
import core.sca as sca

def runTestInputs(code, testInput):
  functions = code.findFunctions()
  newLongCode = code.longCode + f"\noutput = {functions['name'][0]}({testInput})"

  try:
    loc = {}
    exec(newLongCode, globals(), loc)
    result = loc['output']
  except Exception as e:
    print(e)
    result = e
  return result

def blackBoxTesting(modelCodeDir: str, studentCodesDir: list, testInputs: list):
  # modelCode file path
  # studentCode file paths
  # list of inputs
  modelCode = sca.scaModules(modelCodeDir)
  studentCodes = []
  for i in range(len(studentCodesDir)):
    studentCodes += [sca.scaModules(studentCodesDir[i])]

  functions = modelCode.findFunctions()
  if len(functions["name"]) != 1: raise ValueError('Please make sure the code only contain 1 function')
  else:
    result = {
      "model": []
    }

    for i in range(len(testInputs)):
      result["model"] += [runTestInputs(modelCode, testInputs[i])]

      for j in range(len(studentCodes)):
        if f"student{j}" in result:
          result[f"student{j}"] += [runTestInputs(studentCodes[j], testInputs[i])]
        else:
          result[f"student{j}"] = [runTestInputs(studentCodes[j], testInputs[i])]

  return result


def testBlackBoxTesting():
  modelCodeDir = "./test_codes/friday/part2_q1/model.py"
  studentCodesDir = [
    "./test_codes/friday/part2_q1/student1.py",
    "./test_codes/friday/part2_q1/student2.py",
    "./test_codes/friday/part2_q1/student3.py",
    "./test_codes/friday/part2_q1/student4.py"
    ]
  testInputs = [
    [
      [1,2,3,4,5,6],
      [6,0,3,4,2,1],
      [2,1,9,4,6,7],
      [3,0,8,4,6,5],
      [1,5,4,3,3,1],
      [6,1,4,4,3,2]
    ]
  ]

  print("\nRunning testBlackBoxTesting...")
  result = blackBoxTesting(modelCodeDir, studentCodesDir, testInputs)
  print(result)
  print("...testBlackBoxTesting Completed!\n")


if __name__ == '__main__':
  testBlackBoxTesting()