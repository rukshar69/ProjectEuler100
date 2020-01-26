

f1 = 1
f2 = 2
sum  =0
endVal = 4000000
while f2<=endVal:
    if f2%2 ==0:
        sum+=f2
    
    temp = f2+f1
    f1=f2 
    f2 = temp

print(sum)