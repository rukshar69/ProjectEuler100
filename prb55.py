
def reverse(x):
  return x[::-1]

def isPalindrome(string):
    rev = reverse(string)
    if rev == string: return True
    return False

def isLychrel(number):
    iteration = 50

    for i in range(iteration):
        newNum = number + int(reverse(str(number)))
        if isPalindrome(str(newNum)):
            return False
        number = newNum
    return True

lychrelCount = 0
for i in range(1,10000):
    if isLychrel(i):
        lychrelCount+=1

print(lychrelCount)