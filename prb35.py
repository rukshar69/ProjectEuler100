
n = 1000000
prime = [True for i in range(n + 1)] 
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False

SieveOfEratosthenes(n)
#print(sum(prime))
count = 0
def numberofDigits(n): 
    cnt = 0
    while n > 0: 
        cnt += 1
        n //= 10
    return cnt 
      
# function to print the left shift numbers 
def cal(num): 
    global count
    digit = numberofDigits(num) 
    powTen = pow(10, digit - 1) 
    flag = True
    for i in range(digit - 1): 
          
        firstDigit = num // powTen 
          
        # formula to calculate left shift  
        # from previous number 
        left = (num * 10 + firstDigit - 
               (firstDigit * powTen * 10)) 
        #print(left, end = " ") 
        if prime[left]==False:
            flag = False
            break
          
        # Update the original number 
        num = left 
    
    if flag : count += 1
          
# Driver code 
#num = 2
#cal(num) 

for i in range(2,1000000):
    if prime[i]:
        cal(i)

print(count)
  
