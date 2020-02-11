

currentNum = 1 
currentDem = 2

finalNum = currentDem+currentNum
finalDem = currentDem

print(str(finalNum)+'/'+str(finalDem))

count = 0
for i in range(2,1001):
    tempDem = 2*currentDem + currentNum
    tempNum = currentDem

    currentNum = tempNum
    currentDem = tempDem

    finalNum = currentDem+currentNum
    finalDem = currentDem

    lenNum = len(str(finalNum))
    lenDem = len(str(finalDem))
    if lenDem<lenNum: count+=1


    #print(str(finalNum)+'/'+str(finalDem))

print(count)