fname = 'names.txt'
f = open(fname,'r')
f1 = f.readlines()
names = f1[0].split(',')
#print(len(names))
n = len(names)
#print(len(names[200]))
total = 0
names = sorted(names)
print(names[:10])
for i in range(n):
    index = i+1
    name = names[i]
    nameVal = 0
    nameLen = len(name)
    for j in range(1,nameLen-1):
        nameVal += (ord(name[j])- ord('A')+1)
    total += (index * nameVal)

print(total)