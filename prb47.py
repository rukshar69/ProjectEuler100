import math

# A function to print all prime factors of  
# a given number n 
def primeFactors(n):
    factors = [] 
      
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        factors.append(2)
        n = n // 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            factors.append(i)
            n = n // i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        factors.append(n)
    return set(factors)


i =2
limit = 4
while True:
    flag = False
    count = 0
    #print(i)
    for j in range(i,i+limit):
        lenSet = primeFactors(j)
        if len(lenSet) != limit:
            #rint(lenSet)
            break
        else: 
            count+=1
            #print(i)
    if count == limit: break
    i+=1

print(i)
