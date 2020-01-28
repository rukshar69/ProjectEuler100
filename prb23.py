import math
limit = 28124
status = [-1 for i in range(limit)]
#0 perfect 1 abundant 2 deficient
# method to print the divisors 
def sumDivisors(n) : 
      
    # Note that this loop runs till square root 
    i = 2
    total = 0
    while i <= math.sqrt(n): 
          
        if (n % i == 0) : 
              
            # If divisors are equal, print only one 
            if (n // i == i) : 
                total += i
            else : 
                # Otherwise print both 
                total+=( i + n//i) 
        i = i + 1
    return total+1

for i in range(2,limit):
    tempSum = sumDivisors(i)
    if(i == tempSum) :status[i] = 0
    elif(i < tempSum) :status[i] = 1
    else: status[i] = 2

sum = (23*24)//2 #first 23 numbers sum

def isPossible(num):
    lim = num//2 + 1
    for i in range(1,lim):
        if status[i] == 1 and status[num-i] == 1:
            return True #sum of 2 abundant numbers
    return False

for i in range(25, limit):
    number = i
    if isPossible(number)==False:
        sum+= number

print(sum)




