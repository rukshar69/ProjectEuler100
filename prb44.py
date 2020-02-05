import math

def isPentagon(num):
    r = math.sqrt(1+24*num)
    return r%6==5

def pentagon(x):
    n = x * (3 * x - 1) 
    n //=2
    return n

for i in range(1,5000):
    pi = pentagon(i)
    for j in range(i+1,5000):
        pj = pentagon(j)
        s = pi+pj
        d = pj-pi
        if isPentagon(s) and isPentagon(d):
            print(d)