# basic imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from os.path import exists
from rich import print

# import forked core codes
import core.pycode_similar_fork.pycode_similar.pycode_similar as pycode_similar
from core.scoss_fork.scoss import scoss
from core.scoss_fork.scoss import smoss

# import other core codes
import sca

### MAIN ANALYTIC TOOLS ###
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
  unifiedDiff = []
  treeDiff = []
  for i in range(1,len(inputCodes)):
    try:
      unifiedDiffResults = pycode_similar.detect(
          [inputCodes[0], inputCodes[i]], 
          diff_method=pycode_similar.UnifiedDiff, 
          keep_prints=True, 
          module_level=False
        )
      treeDiffResults = pycode_similar.detect(
          [inputCodes[0], inputCodes[i]], 
          diff_method=pycode_similar.TreeDiff, 
          keep_prints=True, 
          module_level=False
        )
      unifiedDiff += [unifiedDiffResults[0][1][0].plagiarism_percent]
      treeDiff += [treeDiffResults[0][1][0].plagiarism_percent]

      # print("source1", studentFileNames[i])
      # print("unifiedDiff", unifiedDiffResults[0][1][0].plagiarism_percent)
      # print("treeDiff", treeDiffResults[0][1][0].plagiarism_percent)
    except Exception as e:
      print(e)
      unifiedDiff += [0]
      treeDiff += [0]
    
  
  df = pd.DataFrame(
    {'source1': studentFileNames,
     'unified_diff': unifiedDiff,
     'tree_diff': treeDiff
    }
  )

  return df

def moss_analysis(modelCodeDir : str, studentCodesDir : list):
    sm = smoss.SMoss(lang='py')
    # print(sm.get_userid())
    sm.add_file(modelCodeDir)
    for directory in studentCodesDir:
        sm.add_file(directory)

    sm.set_threshold(0.0)
    sm.run()

    # print(sm.get_matches())
    return sm.get_matches()


def scoss_analysis(modelCodeDir : str, studentCodesDir : list):

  sc = scoss.Scoss(lang='py')
  sc.add_metric('count_operator', threshold=0) 
  sc.add_metric('set_operator', threshold=0)
  sc.add_metric('hash_operator', threshold=0)

  sc.add_file(modelCodeDir)
  for directory in studentCodesDir:
    sc.add_file(directory)

  sc.run()
  return sc.get_matches(and_thresholds=True)

### DATAFRAME CLEANUP FUNCTIONS ###
def convert_to_dataframe(data, normalise=False):
  if normalise:
    df = pd.json_normalize(data, sep='_')
  else:
    df = pd.DataFrame.from_dict(data)
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
  exercise_marks = []
  max_marks = []
  student_percentage = []
  for index, row in results_df.iterrows():
      student_id, exercise = get_details(row['source1'])
      row = marks_df.loc[marks_df['Student'] == student_id]
      exercise_marks += [int(row[exercise])]
      max_marks += [int(max_marks_row[exercise])]
      student_percentage += [round(int(row[exercise])/int(max_marks_row[exercise]),4)]

  
  results_df['max_mark'] = max_marks
  results_df['real_mark'] = exercise_marks
  results_df['real_percentage'] = student_percentage
  return results_df


### MAIN ###
def analyse(exercise, data):
  # exercise = A, B, C or D

  # SETUP
  marks_df = pd.read_csv('./data/overall_marks.csv')
  modelCodeDir = f"./data/Markscheme/{exercise}_solution.py"
  # we are using 2 to 30 to train, 31 to 40 to test
  # note C28 and C1 does not exist

  # train = train[1:4]
  studentCodesDir = []
  for i in data:
    studentCodesDir += [f"./data/{exercise}/{i}_{exercise}.py"]


  # SCOSS Analysis
  results_dict = scoss_analysis(modelCodeDir, studentCodesDir)
  df1 = convert_to_dataframe(results_dict, normalise=True)
  df1 = df1.rename(
    columns={
      "scores_count_operator": "SCOSS_count",
      "scores_set_operator": "SCOSS_set",
      "scores_hash_operator": "SCOSS_hash"
    }
  )
  # remove data that is now compared to model code
  df1 = df1.drop(df1[df1.source2 != f"./data/Markscheme/{exercise}_solution.py"].index)
  df1 = df1.sort_values('source1')
  df1 = df1.reset_index(drop=True)
  df1 = remove_filepaths(df1)
  df1 = add_marks_to_results(marks_df, df1)
  df1.to_csv(f'data/Results/{exercise}_scoss_results.csv')

  # Pycode Similar Analysis - reading from csv because it is super slow
  if exists(f'data/Results/{exercise}_pysimilar_results.csv'):
    df2 = pd.read_csv(f'data/Results/{exercise}_pysimilar_results.csv')
  else:
    df2 = pycode_similar_analysis(modelCodeDir, studentCodesDir)
    df2 = df2.sort_values('source1')
    df2.to_csv(f'data/Results/{exercise}_pysimilar_results.csv')

  # combine these 2 into 1 final df (they have same source1 vals)
  df = pd.merge(df1, df2, on="source1")

  # arranging df so that actual marks is at the end
  cols = df.columns.tolist()
  df = df[["source1", "source2", "real_mark", "max_mark", "real_percentage", "SCOSS_count", "SCOSS_set", "SCOSS_hash", "unified_diff", "tree_diff"]]
  # print(df)

  return df



if __name__ == '__main__':
  data = ["C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13", "C14", "C15",
          "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C29", "C30",
          "C31", "C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39", "C40"]
  analyse("ExA", data)
  analyse("ExB", data)
  analyse("ExC", data)
  analyse("ExD", data)