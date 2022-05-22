# basic imports
import numpy as np
import pandas as pd
import os
from rich import print

# import forked core codes
import core.pycode_similar_fork.pycode_similar.pycode_similar as pycode_similar
from core.scoss_fork.scoss import Scoss

# import other core codes
import sca

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
  return sc.get_matches(and_thresholds=True)

def convert_to_dataframe(data):
  df = pd.json_normalize(data, sep='_')
  return(df)

def get_details(filepath):
  file = os.path.basename(filepath)
  file_name, file_extension = file.split(".")
  student_id, exercise = file_name.split("_")
  return student_id, exercise

def remove_filepaths(results_df):
  results_df['source1'] = results_df['source1'].apply(os.path.basename)
  results_df['source2'] = results_df['source2'].apply(os.path.basename)
  return results_df

def add_marks_to_results(marks_df, results_df):
  # make sure indexes pair with number of rows
  results_df = results_df.reset_index()  
  marks_df = marks_df.reset_index()
  max_marks_row = marks_df.loc[marks_df['Student'] == "Max"]
  # exercise_marks = []
  # max_marks = []
  student_percentage = []
  for index, row in results_df.iterrows():
      student_id, exercise = get_details(row['source1'])
      row = marks_df.loc[marks_df['Student'] == student_id]
      # exercise_marks += [int(row[exercise])]
      # max_marks += [int(max_marks_row[exercise])]
      student_percentage += [round(int(row[exercise])/int(max_marks_row[exercise]),2)]

  # results_df['Actual Marks'] = exercise_marks
  # results_df['Max Marks'] = max_marks
  results_df['Actual Percentage'] = student_percentage
  return results_df

def analyse(exercise):
  # exercise = A, B, C or D

  marks_df = pd.read_csv('./data/overall_marks.csv')
  # print(marks_df)
  modelCodeDir = f"./data/Markscheme/{exercise}_solution.py"
  # we are using 2 to 30 to train, 31 to 40 to test
  # note C28 and C1 does not exist

  train = ["C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13", "C14", "C15", \
           "C16", "C17", "C18", "C19", "C20", "C22", "C23", "C24", "C25", "C26", "C27", "C29", "C30"]

  test  = ["C31", "C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39", "C40"]

  studentCodesDir = []
  for i in train:
    studentCodesDir += [f"./data/{exercise}/{i}_{exercise}.py"]

  # method 1
  results_dict = scoss_analysis(modelCodeDir, studentCodesDir)
  results_df = convert_to_dataframe(results_dict)
  # remove data that is now compared to model code
  results_df = results_df.drop(results_df[results_df.source2 != f"./data/Markscheme/{exercise}_solution.py"].index)
  results_df = results_df.sort_values('source1')
  results_df = results_df.reset_index(drop=True)
  results_df = remove_filepaths(results_df)
  results_df = add_marks_to_results(marks_df, results_df)
  results_df.to_csv(f'data/Results/{exercise}_scoss_results.csv')
  
  
  # method 2 - currently not working
  result2 = pycode_similar_analysis(modelCodeDir, studentCodesDir)
  print(result2)
  # print(result)


  return results_df


if __name__ == '__main__':
  main()