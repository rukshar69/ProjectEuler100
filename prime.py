

def isPrime(num):
    flag = True
    for i in range(2, num//2):
        if (num % i) == 0: 
            flag = False
            break
        
    if(flag): return True
    return False

n = 2
count = 0
num = 0
while count<=10001:
    if isPrime(n):
        count+=1
        num = n
        #print(count)
    
    n+=1

print(num)