def fiveDigPattern():
    ret = []
    ret.append([1,0,0,0,1])
    ret.append([0,1,0,0,1])
    ret.append([0,0,1,0,1])
    ret.append([0,0,0,1,1])

    return ret

def sixDigPattern():
    ret = []
    ret.append([1, 1, 0, 0, 0, 1 ])
    ret.append([1, 0, 1, 0, 0, 1 ])
    ret.append([ 1, 0, 0, 1, 0, 1 ])
    ret.append([1, 0, 0, 0, 1, 1 ])
    ret.append([ 0, 1, 1, 0, 0, 1])
    ret.append([ 0, 1, 0, 1, 0, 1])
    ret.append([  0, 1, 0, 0, 1, 1 ])
    ret.append([ 0, 0, 1, 1, 0, 1])
    ret.append([ 0, 0, 1, 0, 1, 1 ])
    ret.append([0, 0, 0, 1, 1, 1])

    return ret
#print(sixDigPattern())

def basicPattern(pattern,number):
    
    t = number
    sz = len(pattern)
    filledPattern = [0 for i in range(sz)]
    for i in range(sz-1,-1,-1):
        if pattern[i] == 1:
            filledPattern[i] = t%10
            t//=10
        else: filledPattern[i]=-1
    return filledPattern

def genNumber(repeatingDig, tempPattern):
    sz = len(tempPattern)
    n = 0
    for i in range(sz):
        n *=10
        if tempPattern[i] ==-1: n += repeatingDig
        else: n += tempPattern[i]
    return n

def isPrime(num):
    i = 2
    
    while i*i <=num:
        if num%i == 0: return False
        #if num%(i+2) ==0: return False
        i+=1
    return True

#print(isPrime(23))

def familySet(reapeatingDig, tempPattern):
    fam = 1
    for i in range(reapeatingDig+1,10):
        t = genNumber(i, tempPattern)
        if isPrime(t): fam+=1
    
    #print(fam)
    return fam==8

five = fiveDigPattern()
six = sixDigPattern()
result = 99999999

for i in range(101,1000,2):
    if i%5==0: continue

    usedPattern = []
    if i<100: 
        usedPattern = five
    else: 
        usedPattern = six
        #print('six')

    for j in range(len(usedPattern)):

        for k in range(3):
            if usedPattern[j][0] == 0 and k ==0: continue
            tPattern = basicPattern(usedPattern[j],i)
            candidateNumber = genNumber(k,tPattern)
            
            if candidateNumber<result and isPrime(candidateNumber) and familySet(k,tPattern):              
                    result = candidateNumber
                

print(result)



