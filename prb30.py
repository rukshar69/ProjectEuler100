

upperLim = 6*(9**5)
powers = [i**5 for i in range(0,10)]
def powerSum(num):
    summation = 0
    while num>0:
        rem = num%10
        summation+= powers[rem]
        num //=10
    return summation

total =0
for i in range(10, upperLim+1):
    if(i == powerSum(i)):
        total += i

print(total)