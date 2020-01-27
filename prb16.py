
n = 2**1000
s = str(n)
summation = 0
length = len(s)
for i in range(length):
    c = s[i]
    dig = ord(c) - ord('0')
    summation += dig

print(summation)