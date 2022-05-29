

import math

def sum(n):
    cid = '01704452'
    if n <= 1:
        return 1
    return math.pow(n, int(cid[5])) / math.factorial(n-1) + sum(n-1)

print(sum(15))