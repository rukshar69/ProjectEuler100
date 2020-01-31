

factorials = [1 for i in range(10)]
for  i in range(1,10):
    factorials[i] = factorials[i-1]*i

def sumOfDig(num):
    total =0
    while num>0:
        dig = num%10
        total += factorials[dig]
        num //=10
    return total


#print(sumOfDig(145))
tot = 0
for i in range(10,9999999):
    if i == sumOfDig(i):
        tot += i
print(tot)
