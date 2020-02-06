maxn = 1000000
primes = [ True for i in range(maxn)]
primeList = []

def sieve():
    primes[0] = False
    primes[1] = False

    i = 2
    while i<maxn:
        if primes[i]==True:
            primeList.append(i)
            for j in range(i*2, maxn,i):
                primes[j] = False
        i+=1
sieve()

primeLen = len(primeList)
#print(primeList)
maxSum = -1
maxRun  = -1
for i in range(primeLen):
    total = 0
    for j in range(i, primeLen):
        total += primeList[j]
        if total>= maxn:
            break
        #print(total)
        if primes[total] and maxSum<total and j - i>maxRun:
            maxRun = j-i
            maxSum = total

print(maxSum)
