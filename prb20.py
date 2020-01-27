prd = 1
for i in range(1,101):
    prd *= i

print(prd)
prd = str(prd)
n = len(prd)
summation = 0
for i in range(n):
    digit = ord(prd[i]) - ord('0')
    summation+=digit

print(summation)