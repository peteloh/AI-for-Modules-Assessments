test_code_string = """
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
"""

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

class code:
    def __init__(self, filename):
        if filename[-3:] == ".py":
            f = open(filename,'r')
            codelines = f.readlines()
            self.strings = codelines
        else:
            # filename is the string
            self.strings = filename.splitlines()
    
    def find_operator(operator):
        found = []
        for i in range(len(self.strings)):
            operator_index = self.strings[i].find(operator)
            comment_index = self.strings[i].find("#")
            if operator_index != -1:
                # the string exist in that line but is  it commented?
                if comment_index == -1: found += [i]
                else:
                    if operator_location < comment_location: return operator_location
                    # else operator is being commented so doesnt count         


            if index != -1: found += [index]
        if found == []: self.find_if = -1
        else: self.find_if = index

    def find_ifs():
            found = []
            for line in self.strings:
                index = line.find("if")
                if index != -1: found += [index]
            if found == []: self.find_if = -1
            else: self.find_if = index




# code1 is a codestring in the file
code1 = code(test_code_string)
print(code1.strings)

# code2 is a filename for another code in the same directory
code2 = code(test_file)
print(code2.strings)
