
def collatz(num):
    count = 1
    while num!=1:
        count +=1
        if num %2 == 0:
            num = num//2
        else: 
            num = 3*num+1
        
    
    return count

maximum = -1
max_seqlen = -1

for i in range(1000000, 1, -1):
    sz = collatz(i)
    if sz>max_seqlen: 
        maximum = i
        max_seqlen = sz
print(maximum)