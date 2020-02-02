
def decimalToBinary(n):  
    return bin(n).replace("0b", "")
def isPalindrome(string):
    return string==string[::-1]

total = 0
for i in range(1,1000000):
    binary = decimalToBinary(i)
    if(isPalindrome(str(i)) and isPalindrome(str(binary))):
        total += i

print(total)
