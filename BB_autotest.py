# code_strings = """
# def triangle(x: int, y: int, z: int) -> str:
#     if x == y == z:
#         return "Equilateral triangle"
#     elif x == y or y == z or x == z:
#         return "Isosceles triangle"
#     else:
#         return "Scalene triangle"
# """


def python_to_string(file):
    code_strings = ""
    f = open(file,'r')
    codelines = f.readline()
    print(codelines[1])
    # for line in lines

python_to_string("BB_test_code.py")


# def find_conditionals(code_strings):

