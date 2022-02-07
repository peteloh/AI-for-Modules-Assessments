import ast

code1 = b"""
x = 0
while x<=10: # should run 10 times
    x+=1
"""

code2 = b"""
for i in range(0,5):
    continue
"""

code3 = b"""
z = False
for i in range(0,5):
    if z == True:
        x = 0
        while x<=10: # should run 10 times
            x+=1
"""

class for_loop(ast.NodeVisitor):
    def visit_For(self, node):
        print(f"Visiting for loop at line {node.lineno}")

class while_loop(ast.NodeVisitor):
    def visit_While(self, node):
        print(f"Visiting while loop at line {node.lineno}")

check_code = code3

visitor1 = for_loop()
visitor2 = while_loop()

tree = ast.parse(check_code)
visitor1.visit(tree)
visitor2.visit(tree)


