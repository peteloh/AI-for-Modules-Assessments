# Ex 4
def fact(n):
    if n == 0:
        res = 1
    else:
        res = n * fact(n-1)
    return res

def sum(i):
    if i == 1:
        res = 1
    else:
        res = sum(i-1) + i**b[5]/fact(i-1)
    return res

print(sum(15))