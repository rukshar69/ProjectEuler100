upperBound = 1000000
maxN = 100
count = 0
factorials=[1 for i in range(101)]
def fillupFactorials():
    for i in range(2,101):
        factorials[i] = factorials[i-1]*i

def factorial(num):
    return factorials[num]
def solution1():
    global count
    for n in range(1,maxN+1):
        for r in range(0,n+1):
            combo = factorial(n) //(factorial(r)*factorial(n-r))
            if combo >= upperBound: count+=1

fillupFactorials()
solution1()
print(count)

#print(factorial(10))