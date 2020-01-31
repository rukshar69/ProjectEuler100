

from fractions import gcd





nominator =1
denom = 1
for n in range(1,10):
    for d in range(n+1,10):
        for c in range(d+1,10):
            if(10*n+c)*d == (10*c+d)*n:
                nominator *= n
                denom *= d


denom = denom// gcd(nominator,denom)
print(denom)

