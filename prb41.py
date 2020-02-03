
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

from itertools import permutations 

max = -1
for i in range(3,10):

    print('creating list')
    l = list(permutations(range(1, 8))) 
    print('list done')
    
    for num in l:
        num = ''.join(map(str,num))
        num = int(num)
        #print(num)
        if isPrime(num):
            #print(num)
            if num>max: 
                max = num
            

print(max)