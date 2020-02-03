import math

fname = 'word.txt'
f = open(fname, 'r')
wordList = f.readlines()
wordList = wordList[0].split(',')

wordList =[ a.replace('"', '') for a in wordList]

def valueWord(word):
    n = len(word)
    total = 0
    for i in range(n):
        total += (ord(word[i])-ord('A')+1)
    return total

print(wordList[:5])
wordList = [valueWord(w) for w in wordList]
print(wordList[:5])

def isTriangular(num): 
  
    if (num < 0): 
        return False
  
    # Considering the equation n*(n+1)/2 = num 
    # The equation is : a(n^2) + bn + c = 0 
    c = (-2 * num) 
    b, a = 1, 1
    d = (b * b) - (4 * a * c) 
  
    if (d < 0): 
        return False
  
    # Find roots of equation 
    root1 = ( -b + math.sqrt(d)) / (2 * a) 
    root2 = ( -b - math.sqrt(d)) / (2 * a) 
  
    # checking if root1 is natural 
    if (root1 > 0 and math.floor(root1) == root1): 
        return True
  
    # checking if root2 is natural 
    if (root2 > 0 and math.floor(root2) == root2): 
        return True
  
    return False
  
wordList = [isTriangular(num) for num in wordList]

print(sum(wordList))
