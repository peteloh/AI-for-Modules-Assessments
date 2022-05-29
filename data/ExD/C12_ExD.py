#CID = 01712921







#Factorial function needed to calculate the factorial in denominator of series expansion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


#Recursion formula
def Recursion(i):
    if i == 1:
        S = 1
    else:
        S = ((i)**9)/(factorial(i-1)) + Recursion(i-1)
    return S

#tested it by inputting 2
a = Recursion(2)
print(a)



























