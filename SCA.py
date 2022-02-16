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
            self.long_string = remove_comments_and_docstrings(f.read())
            self.lines = self.long_string.splitlines()

        else:
            # filename is the codestring already
            self.long_string_with_comments = filename
            self.long_string = remove_comments_and_docstrings(filename)
            self.lines = self.long_string.splitlines()
    
    def find_functions(self):
        # classes so no need to detect functions in classes
        functions = [] # [row,name]
        for row in self.lines:
            if row.find("def") != -1:
                start = 4 # function name starts at 5th character [def + space + function name]
                for j in range(4,len(row)):
                    if row[j] == "(" :
                        end = j
                        functions += [row[start:end]]
                        break
        return functions

    def find_operator(self, operator : str):
        valid_operators = ["if","elif","else","for","while"]
        if operator not in valid_operators : raise ValueError
        location = []
        if operator == "if":
            for row in range(len(self.lines)):
                index1 = self.lines[row].find(operator)
                index2 = self.lines[row].find(" " + operator + " ") # this makes sure that if not found at the start of line, it should be a seperate word
                if index1 == 0 : location += [index1]
                elif index2 != -1 : location += [index2 + 1]
        else:
            for row in range(len(self.lines)):
                index = self.lines[row].find(operator)
                if index != -1 : location += [index]

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
        for_loops = code.find_operator("for")
        if for_loops != None:
            for loop in for_loops: total_loops += [loop]
    
    if 'While Loop' in loop_to_check:
        while_loops = code.find_operator("while")
        if while_loops != None:
            for loop in while_loops: total_loops += [loop]

    indentation = []
    for i in total_loops:
        if i not in indentation: indentation += [i]
    
    return len(indentation)


def detect_indentation(line):
    return len(line) - len(line.lstrip())


CODE1_FILENAME = "while_loop_nested.py"
CODE2_STRING = """
# comment 1
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle" #comment 2
"""
CODE3_STRING = """
print("Hi")
"""

if __name__ == '__main__': 
    
    code = analyse(CODE1_FILENAME)
    print(code.lines)

    print(code.find_functions())

    print(find_nested_loops(code))
