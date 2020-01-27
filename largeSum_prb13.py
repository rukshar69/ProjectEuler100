fname = 'number.txt'
f = open(fname, 'r')
f1 = f.readlines()

#print(f1[0])
sum = [0 for i in range(50)]
remainder = 0
for i in range(49,-1,-1):
    temp_sum = remainder
    for j in range(100):
        temp_sum += (ord(f1[j][i])-ord('0'))
    dig = temp_sum%10
    sum[i] = dig
    remainder = temp_sum//10

#print(remainder)
s = str(remainder) + ''.join(map(str, sum[:8]))
print(s)