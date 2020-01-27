from math import *

# Function to calculate the number of divisors of integer n
def divisors(n):
    limit = int(sqrt(n))
    divisors_list = []
    for i in range(1, limit+1, 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n/i:
                divisors_list.append(n/i)
    return len(divisors_list)
                

seriesLastTerm = 1
check = 1
while divisors(check) <= 500:
    # add the next term to check to get the next triangle number
    check += (seriesLastTerm + 1)
    seriesLastTerm += 1
print (check)