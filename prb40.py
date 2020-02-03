num = 1
string = '0'
d = 1
prd = 1

while True:
    string += str(num)
    num+=1
    if len(string)>d:
        prd*=int(string[d])
        d *= 10
        print(prd)
    if d>1000000:
        break

print(prd)
