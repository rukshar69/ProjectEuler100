def isPerm(a,b):
    freq = [0 for i in range(10)]
    while a>0:
        r = a%10
        freq[r] +=1
        a//=10
    
    while b>0:
        r = b%10
        freq[r] -=1
        b//=10

    for i in range(10):
        if freq[i] != 0: return False
    return True

#print(isPerm(125774,251748))

i = 10
while True:
    multipleList = []
    multipleList.append(i)
    for j in range(2,7):
        multipleList.append(i*j)
    
    #print(len(multipleList))
    flag = True
    for j in range(5):
        n = multipleList[j]
        m = multipleList[j+1]
        if isPerm(n,m)==False: 
            flag = False
            break

    if flag: break
    i += 1
print(i)
