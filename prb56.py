
def digitalSum(number):
    total = 0
    while number>0:
        total += (number%10)
        number //=10
    return total
maximum = -1
def solution():
    global maximum
    for a in range(2,100):
        for b in range(1,100):
            power = a**b
            digSum = digitalSum(power)
            if digSum>maximum : maximum = digSum
    return maximum

print(solution())
