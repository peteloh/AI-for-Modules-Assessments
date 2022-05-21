#CID:01711943#
import math
def Sum(N):
    if N ==1:
        S=1
    else:
        S = N**9/math.factorial(N-1)+Sum(N-1)
    return S

print(Sum(15))
