
visited = [False for i in range(10001)]

import math  
  
# method to print the divisors 
def divisorSum(n) : 
      
    # Note that this loop runs till square root 
    i = 2
    summation = 0
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
              
            # If divisors are equal, print only one 
            if (n // i == i) : 
                summation += i 
            else : 
                # Otherwise print both 
                summation += ( i + n//i)
        i = i + 1
    
    return summation + 1
  
# Driver method 
total = 0
for i in range(1,10001):
    a = i
    b = divisorSum(a)
    c = divisorSum(b)
    if a!=b and a==c and b>a:
        
        total += (b+i)

print(total)