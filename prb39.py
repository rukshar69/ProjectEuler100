import math

dictPerimeter = {}

limit  = 1000

def findC(a,b):
    lim = a+b
    lower = abs(a-b)
    for c in range(lim,lower+1,-1):
        if c*c == a*a + b*b:
            return c
    return -1
def solution():

    half = limit//2
    for a in range(0,half):
        for b in range(0,half):
            c = findC(a,b)

            if c!=-1  and a+b+c<=limit:
                print('c ',c)
                p = a+b+c
                if p in dictPerimeter.keys():
                    dictPerimeter[a+b+c] = dictPerimeter[a+b+c]+1
                else:dictPerimeter[a+b+c] =0


solution()
print(dictPerimeter)
