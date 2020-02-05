import math

def isPentagon(num):
    r = math.sqrt(1+24*num)
    return r%6==5

def isHexagon(num):
    r = 1 + math.sqrt(1+8*num)
    return r%4==0

def triangle(x):
    t = x*(x+1)
    t //=2
    return t

n = 286
found = False
while True:
    number = triangle(n)
    n+=1
    if isPentagon(number) and isHexagon(number):
        print(number)
        break
    
