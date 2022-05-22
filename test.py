# data clean up
import pandas as pd

# columns = ["Student", "Total", "ExA", "ExB", "ExC", "ExD", "Comments"]
# filepath = "./data/overall_marks.csv"

# df = pd.read_csv(filepath, usecols=columns)
# df.dropna(inplace=True)

# print(df)

# students = [i for i in range(2,40+1)]
# print(students)


# import sca as sca
# import os
# exercise = "ExA"
# # filepath = f"./data/Markscheme/{exercise}_solution.py"
# filepath = './data/ExA/C2_ExA.py'
# f = open(filepath,'r')
# filepath = filepath
# longCode = f.read()
# # codeLines = longCode.splitlines()
# # longCodeNoComments = sca.cleanCode(longCode)
# # codeLinesNoComments = longCodeNoComments.splitlines()

# # path, filename = os.path.split(filepath)

# # isFunction = False
# # for codeLine in codeLinesNoComments:
# #     if codeLine.find("def") != -1:  isFunction = True


# import pyparsing

# # commentFilter = pyparsing.cppStyleComment.suppress()
# # To filter python style comment, use
# commentFilter = pyparsing.pythonStyleComment.suppress()
# # To filter C style comment, use
# # commentFilter = pyparsing.cStyleComment.suppress()

# newtest = commentFilter.transformString(longCode)
# print(newtest)

import os

def get_student_id(filepath):
    file = os.path.basename(filepath)
    file_name, file_extension = file.split(".")
    student_id, exercise = file_name.split("_")
    print(student_id, exercise)

get_student_id("./data/ExA/C02_ExA.py")
