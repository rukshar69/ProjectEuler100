
def isPrime(num):
    if num ==1 : return False
    if num==2 or num ==3: return True
    if num%2==0 or num%3==0: return False

    i = 5
    while i*i<=num:
        if num%i ==0 or num%(i+2)==0:
            return False
        i+=6
    return True
def an(n):
    t = 4*n*n
    t+= 4*n
    t+=1
    return t
def bn(n):
    t = 4*n*n
    t+=1
    return t
def cn(n):
    t = 4*n*n
    t-= 2*n
    t+=1
    return t
def dn(n):
    t = 4*n*n
    t+= 2*n
    t+=1
    return t

def solution():
    n = 1
    primes = 0
    iteration = 1
    while True:
        a = an(n)
        b = bn(n)
        c = cn(n)
        d = dn(n)
        if isPrime(a): primes+=1
        if isPrime(b): primes+=1
        if isPrime(c): primes+=1
        if isPrime(d): primes+=1
        totalDiagonalNumbers = 4*n+1
        ratio = primes/totalDiagonalNumbers
        print(iteration,' : ',ratio)
        if ratio<0.1:
            width = 2*n+1
            return width
        iteration +=1
        n+=1

print(solution())