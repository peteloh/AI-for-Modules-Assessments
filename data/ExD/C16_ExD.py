#Write a function that carries out the sum
def SUM(N):
    n = input('Gimme me a number: ')
    n = int(n)

    #Factorials start from 1
    f = 1

    # set the range of the counter, from n to 1 in decremental steps of 1
    for i in range(n-1,0,-1):
    # contribution of the current term to the overall product
        f = f * i
        f = int(f)
    print(f)

    if N == 1:
        print('impossible')
    else:
        S = N**9/f
    return S

N = 15
a = SUM(N)
print(a)