unusuals = []

m1 = 1
n1 = 100
m2 = 123
n2 =9999

def allDigitPresent(string):
    freq = [0 for i in range(10)]
    n = len(string)
    for i in range(n):
        dig = ord(string[i]) - ord('0')
        freq[dig] +=1
    
    flag = True
    for i in range(1,10):
        if freq[i] ==0:
            flag = False
            break
    
    return flag

for i in range(m1,n1):
    for j in range(m2,n2):
        prd = i*j
        s = str(i) + str(j) + str(prd)
        if len(s) == 9 and allDigitPresent(s):
            unusuals.append(prd)

unusuals = set(unusuals)

print(sum(unusuals))


