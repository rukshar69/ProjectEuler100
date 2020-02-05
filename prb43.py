
from itertools import permutations 
l = list(permutations(range(0, 10))) 

primes = [2,3,5,7,11,13,17]

total = 0
for num in l:
    num = ''.join(map(str,num))
    #print(num)
    index = 0
    count = 0
    for i in range(1,8):
        tmp = num[i] + num[i+1]+num[i+2]
        #print(tmp)
        tmp = int(tmp)
        if tmp % primes[index] != 0:
            break
        index+=1
        count +=1
    if count == len(primes):
        print(num)
        total += int(num)

print(total)
    
    