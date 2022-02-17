from io import StringIO
import tokenize

def remove_comments_and_docstrings(source):
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

class analyse:
    def __init__(self, filename):
        if filename[-3:] == ".py":
            f = open(filename,'r')
            self.long_string_with_comments = f.read()
            self.long_string = remove_comments_and_docstrings(self.long_string_with_comments)
            self.lines = self.long_string.splitlines()

        else:
            # filename is the codestring already
            self.long_string_with_comments = filename
            self.long_string = remove_comments_and_docstrings(filename)
            self.lines = self.long_string.splitlines()
    
    def find_functions(self):
        # classes so no need to detect functions in classes
        functions = [] # [row, name]
        for i in range(len(self.lines)):
            if self.lines[i].find("def") != -1:
                start = 4 # function name starts at 5th character [def + space + function name]
                for j in range(4,len(self.lines[i])):
                    if self.lines[i][j] == "(" :
                        end = j
                        functions += [[i, self.lines[i][start:end]]]
                        break
        return functions

    def find_operator(self, operator : str):
        valid_operators = ["if","elif","else","for","while", "return"]
        if operator not in valid_operators : raise ValueError
        location = [] #saves the row and function name
        if operator == "if":
            for row in range(len(self.lines)):
                index1 = self.lines[row].find(operator)
                index2 = self.lines[row].find(" " + operator + " ") # this makes sure that if not found at the start of line, it should be a seperate word
                if index1 == 0 : location += [[row, index1]]
                elif index2 != -1 : location += [[row, index2 + 1]]
        else:
            for row in range(len(self.lines)):
                index = self.lines[row].find(operator)
                if index != -1 : location += [[row, index]]

        if location == []: return None
        else: return location
    
    def run(self):
        try:
            exec(self.long_string)
        except Exception as e:
            raise


def find_nested_loops(code, loop_to_check):
    
    total_loops = []

    if 'For Loop' in loop_to_check:
        for_locations = code.find_operator("for")
        if for_locations != None:
            for_loops = [i[1] for i in for_locations] #i[1] is the indentation
            for loop in for_loops: total_loops += [loop]
    
    if 'While Loop' in loop_to_check:
        while_locations = code.find_operator("while")
        if while_locations != None:
            while_loops = [i[1] for i in while_locations] #i[1] is the indentation
            for loop in while_loops: total_loops += [loop]
    
    if total_loops == []: return "No Loops"

    indentation = []
    for i in total_loops:
        if i not in indentation: indentation += [i]
    
    return len(indentation)


def check_recursive(code):
    # 1. the code has to be a function
    # 2. within the function, it calls itself
    code_functions = code.find_functions()

    if code_functions == []: return False #no function at all

    function_row = [i[0] for i in code_functions]
    return_row = [i[0] for i in code.find_operator("return")] # 1D list now, want just row part

    recursive = False
    for i in range(function_row[0], return_row[0]):
        if code.lines[i].find(code_functions[0][1]) != -1:
            recursive = True
    
    return recursive

if __name__ == '__main__':
    TEST_CODE2 = """
    def Sum(N):
        if N == 2:
            S = 1
        else:
            S = 3**(N-2) + Sum(N-1)
        return S

    #
    a = Sum(5)
    print(a)
    """

    test_code_name = "./test_codes/for_loop1.py"
    test_code = analyse(test_code_name)
    print(check_recursive(test_code))

    # code_functions = test_code.find_functions()
    # print(code_functions)

    # function_row = [i[0] for i in code_functions]
    # print(function_row)
    # return_row = [i[0] for i in test_code.find_operator("return")] # 1D list now, want just row part
    # print(return_row)

    # recursive = False
    # for i in range(function_row[0], return_row[0]):
    #     if test_code.lines[i].find(code_functions[0][1]) != -1:
    #         recursive = True
    
    # print(recursive)

    # print(code_functions, code_returns)
