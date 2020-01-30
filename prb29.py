
import math
numbers = []

upperLim  =101
for i in range(2,upperLim):
    for j in range(2,upperLim):
        power = math.pow(i,j)
        numbers.append(power)

numbers = set(numbers)
print(len(numbers))
