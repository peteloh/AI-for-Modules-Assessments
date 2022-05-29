a = 0
S = 1 # Term 0
def sum(N):
    term = 1/(N-1) #My cid is 0, so i^a = 0
    N += -1
    S *= term # Multiplies the previous terms together
    return S

sum(15)