import ast

# Demo code to parse
code = """\
sheep = ['Shawn', 'Blanck', 'Truffy']

def get_herd():
    herd = []
    for a_sheep in sheep:
        herd.append(a_sheep)
    return Herd(herd=herd)

class Herd:
    def __init__(self, herd):
        self.herd = herd

    def shave(self, setting='SMOOTH'):
        for sheep in self.herd:
            print(f"Shaving sheep {sheep} on a {setting} setting")
"""


class Example(ast.NodeVisitor):
    def visit_For(self, node):
        print(f"Visiting for loop at line {node.lineno}")

tree = ast.parse(code)
visitor = Example()
visitor.visit(tree)

