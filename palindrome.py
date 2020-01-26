

def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    
    return rev

maximum = -1
for i in range(999,99,-1):


    for j in range(999,99,-1):
        temp = i*j
        reverse = palindrome(temp)
        if(temp ==reverse):
            if maximum<temp:
                maximum = temp

print(maximum)