from io import StringIO
import tokenize
import numpy as np
import os

def cleanCode(source):
    """
    Returns 'source' minus comments and docstrings.
    """
    io_obj = StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]
        # The following two conditionals preserve indentation.
        # This is necessary because we're not using tokenize.untokenize()
        # (because it spits out code with copious amounts of oddly-placed
        # whitespace).
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        # Remove comments:
        if token_type == tokenize.COMMENT:
            pass
        # This series of conditionals removes docstrings:
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
        # This is likely a docstring; double-check we're not inside an operator:
                if prev_toktype != tokenize.NEWLINE:
                    # Note regarding NEWLINE vs NL: The tokenize module
                    # differentiates between newlines that start a new statement
                    # and newlines inside of operators such as parens, brackes,
                    # and curly braces.  Newlines inside of operators are
                    # NEWLINE and newlines that start new code are NL.
                    # Catch whole-module docstrings:
                    if start_col > 0:
                        # Unlabelled indentation means we're inside an operator
                        out += token_string
                    # Note regarding the INDENT token: The tokenize module does
                    # not label indentation inside of an operator (parens,
                    # brackets, and curly braces) as actual indentation.
                    # For example:
                    # def foo():
                    #     "The spaces before this docstring are tokenize.INDENT"
                    #     test = [
                    #         "The spaces before this string do not get a token"
                    #     ]
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    return out

class scaTools:
    def __init__(self, filepath : str):
        try:
            f = open(filepath,'r')
            self.filepath = filepath
            self.longCode = f.read()
            self.codeLines = self.longCode.splitlines()
            self.longCodeNoComments = cleanCode(self.longCode)
            self.codeLinesNoComments = self.longCodeNoComments.splitlines()

            path, filename = os.path.split(filepath)
            self.filename = filename
            
            self.isFunction = False
            for codeLine in self.codeLinesNoComments:
                if codeLine.find("def") != -1:  self.isFunction = True
                
        except:
            raise ValueError('Please input correct file path')
    
    
    def findFunctions(self):
        codeLines = self.codeLinesNoComments
        # working with code without any comments
        # {"names": [fn1, fn2...], "startRow": [startRow1, startRow2....], "endRow": [endRow1, endrow2...]}
        functions = {
            "name": [],
            "row": [],
        }
        for row in range(len(codeLines)):
            if codeLines[row].find("def") != -1:
                # function name starts at 5th string of the line
                start = 4 
                for index in range(4,len(codeLines[row])):
                    if codeLines[row][index] == "(" :
                        end = index
                        functions["name"] += [codeLines[row][start:end]]
                        functions["row"] += [row]
                        break
        return functions

    def findOperator(self, operator : str):
        validOperators = [
            "if",
            "elif",
            "else",
            "for",
            "while", 
            "return"
        ]

        if operator not in validOperators : raise ValueError('Invalid Input')

        operatorLocations = {
            "row" : [],
            "index": []
        }

        codeLines = self.codeLinesNoComments
        if operator == "if":
            for row in range(len(codeLines)):
                index1 = codeLines[row].find(operator)
                index2 = codeLines[row].find(" " + operator + " ") # this makes sure that if not found at the start of line, it should be a seperate word
                if index1 == 0 : 
                    operatorLocations["row"] += [row]
                    operatorLocations["index"] += [index1]
                elif index2 != -1 :
                    operatorLocations["row"] += [row]
                    operatorLocations["index"] += [index2 + 1]

        else:
            for row in range(len(codeLines)):
                index = codeLines[row].find(operator)
                if index != -1 :
                    operatorLocations["row"] += [row]
                    operatorLocations["index"] += [index]

        return operatorLocations
    
    def convertToFunction(self):
        if self.isFunction == True: return self.longCode
        else:
            newFirstLine = "def foo():"
            indentation = "    "
            codeLines = self.codeLines

            newLongCode = newFirstLine
            for line in codeLines:
                newLongCode += ("\n" + indentation + line)

            return newLongCode


class scaModules(scaTools):
    def countNestedLoops(self, checklist):
        validChecklistInput = [
            ["for"],
            ["while"],
            ["for","while"]
        ]

        if checklist not in validChecklistInput : raise ValueError('Invalid Input')

        indentations = []

        for loopName in checklist:
            loopOperatorLocations = self.findOperator(loopName)
            indexes = loopOperatorLocations["index"]
            if indexes != []: indentations += [indexes]
        
        # count different indentationLevels
        numberNestedLoops = len(np.unique(indentations))

        return numberNestedLoops
    
    def isRecursive(self):
        # this works for 1 function recursion, does not work for multiple
        if self.isFunction == False: return False

        functions = self.findFunctions()
        if len(functions["name"]) != 1: raise ValueError('Please make sure the code only contain 1 function')

        functionName = functions["name"][0]
        functionRow = functions["row"][0]

        checkingString = f" {functionName})"
        codeLines = self.codeLinesNoComments

        checkLine = codeLines[functionRow+1]
        firstIndentation = len(checkLine) - len(checkLine.lstrip())

        functionLastRow = None

        for i in range(functionRow+1,len(codeLines)):
            if codeLines[i].find(firstIndentation*" ") == -1: functionLastRow = i
        
        if functionLastRow == None: return len(codeLines)-1
        
        for i in range(functionRow+1, functionLastRow):
            if codeLines[i].find(functionName) != -1: return True
        
        return False
    
    def readsFile(self):
        codeLines = self.codeLinesNoComments

        for i in range(len(codeLines)):
            if codeLines[i].find("open") != -1: return True
        
        return False
                    

def testCountNestedLoops():
    print("\nRunning testCountNestedLoops...")
    fileLocation1 = "./test_codes/basic/for_loop_nested.py"
    code1 = scaModules(fileLocation1)
    print(f"Result 1 = {code1.countNestedLoops(['for','while'])}")
    print("Expected 1 = 3")
    print("...testCountNestedLoops Completed!\n")

def testIsRecursive():
    print("\nRunning testIsRecursive...")
    fileLocation1 = "./test_codes/basic/for_loop_nested.py"
    code1 = scaModules(fileLocation1)
    print(f"Result 1 = {code1.isRecursive()}")
    print("Expected 1 = False")

    fileLocation2 = "./test_codes/basic/recursive_code1.py"
    code2 = scaModules(fileLocation2)
    print(f"Result 2 = {code2.isRecursive()}")
    print("Expected 2 = True")
    print("...testIsRecursion Completed!\n")

def testCodeReadsFile():
    print("\nRunning testCodeReadsFile...")
    fileLocation1 = "./test_codes/basic/read_file.py"
    code1 = scaModules(fileLocation1)
    print(f"Result 1 = {code1.readsFile()}")
    print("Expected 1 = True")

    fileLocation2 = "./test_codes/basic/while_loop1.py"
    code2 = scaModules(fileLocation2)
    print(f"Result 2 = {code2.readsFile()}")
    print("Expected 2 = False")
    print("...testCodeReadsFile Completed!\n")

def testNonFunctions():
    print("\nRunning testNonFunctions...")
    fileLocation1 = "./test_codes/basic/not_a_function.py"
    code1 = scaModules(fileLocation1)
    print(f"Result 1 = {code1.countNestedLoops(['for','while'])}")
    print("Expected 1 = 2")
    print(f"Result 2 = {code1.isRecursive()}")
    print("Expected 2 = False")
    print(f"Result 3 = {code1.readsFile()}")
    print("Expected 3 = True")
    print("...testCountNestedLoops Completed!\n")

def testConverToFunction():
    fileLocation1 = "./test_codes/basic/not_a_function.py"
    code1 = scaModules(fileLocation1)
    print(code1.longCode)
    print(code1.convertToFunction())


if __name__ == '__main__':
    # testCountNestedLoops()
    # testIsRecursive()
    # testCodeReadsFile()
    # testNonFunctions()
    # testConverToFunction()
    pass


