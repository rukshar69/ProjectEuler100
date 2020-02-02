
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def rightAllPrime(n):
    while n>=1:
        if isPrime(n) == False:
            return False
        n//=10
    return True

def leftAllPrime(n):
    s = str(n)
    l = len(s)
    
    while l>=1:
        number = int(s)

        if isPrime(number)==False: 
            
            return False
        if l>1:
            s = s[1:]
        l-=1
    return True
primeCount = 0
num = 21

total = 0

while True:

    if isPrime(num) and rightAllPrime(num) and leftAllPrime(num):
        total+=num
        primeCount +=1
        print(primeCount)
        print(num)
    
    if primeCount==11: break
    num+=1

print(total)



'''
num = 3797
if isPrime(num) :
    print('prime')
    if rightAllPrime(num):
        print(  'right')
        if leftAllPrime(num):
            print('here')
else: print('no')
'''
