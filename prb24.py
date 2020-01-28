
limit = 3
numbers = [i for i in range(limit)]

from itertools import permutations 
l = list(permutations(range(0, 10))) 
s = l[999999] 
st = "".join(map(str,s))
print(st)