

f1 = 1
f2 = 1
index = 2
length = 1
while length<1000:
    temp = f1+f2
    f1 = f2
    f2 = temp
    index+=1
    length = len(str(f2))

print(index)