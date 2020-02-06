maxn = 9999
primes = [ True for i in range(maxn)]

def sieve():
    primes[0] = False
    primes[1] = False

    i = 2
    while i*i<=maxn:
        if primes[i]==True:
            for j in range(i*2, maxn,i):
                primes[j] = False
        i+=1
sieve()

def isPrime(num):
    return primes[num] 

def isCombo(n1,n2):
    freq = [0 for i in range  (10)]
    while n1>0:
        r = n1%10
        freq[r] +=1
        n1//=10

    while n2>0:
        r = n2%10
        freq[r] -=1
        n2//=10
    
    for i in range(10):
        if freq[i] != 0 : return False

    return True
def solution():
    for a in range(1489, 3340):
        b= a+3330
        c = b+3330
        if isPrime(a) and isPrime(b) and isPrime(c) and isCombo(a,b) and isCombo(b,c):
            return str(a)+str(b)+str(c)


print(solution())