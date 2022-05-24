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

def test_smoss(modelCodeDir : str, studentCodesDir : list):
    sm = smoss.SMoss(lang='py')
    # print(sm.get_userid())

    sm.add_file(modelCodeDir)
    for directory in studentCodesDir:
        sm.add_file(directory)

    sm.set_threshold(0.0)
    sm.run()

    result = sm.get_matches()
    print(result)
    return result
    # print(sm.get_similarity_matrix())

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


def main():
    exercise = "ExA"
    modelCodeDir = f"./data/Markscheme/{exercise}_solution.py"
    # we are using 2 to 30 to train, 31 to 40 to test
    # note C28 and C1 does not exist
    train = ["C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11", "C12", "C13", "C14", "C15", \
            "C16", "C17", "C18", "C19", "C20", "C22", "C23", "C24", "C25", "C26", "C27", "C29", "C30"]
    test  = ["C31", "C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39", "C40"]

    studentCodesDir = []
    for i in train:
        studentCodesDir += [f"./data/{exercise}/{i}_{exercise}.py"]

    result = test_smoss(modelCodeDir, studentCodesDir)
    df2 = df = pd.DataFrame.from_dict(result)
    # df2 = df2.sort_values('source1')
    df2.to_csv(f'data/Results/{exercise}_moss_results.csv')

    # print(scoss_analysis(modelCodeDir, studentCodesDir))










if __name__ == '__main__':
    # python3 tests/test_scoss.py 
    # 1. url variable will be empty if userid is invalid
    # userid should be 5-digit long, e.g. 13579
    # 2. maybe moss server takes forever to return
    main()
