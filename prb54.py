fname = 'poker.txt'
f = open(fname,'r')

games = f.readlines()
games = [s.split(' ') for s in games]
player1 = []
player2=[]
for hand in games:
    player1.append(hand[:5])
    player2.append(hand[5:])

#print(player2[:5])
value = {'A':14,'K':13,'Q':12,'J':11,'T':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2,'1':1}

def isSameSuit(hand):
    suit = hand[0][1]
    for i in range(1,5):
        s = hand[i][1]
        if s!= suit: return False
    return True

def valuesOfHand(hand):
    vals = []
    for h in hand:
        c  = h[0]
        vals.append(value[c])
    vals.sort()
    return vals

def frequency(vals):
    freq = [0 for i in range(15)]
    for k in vals:
        freq[k] += 1
    return freq

def royalFlush(hand):
    if isSameSuit(hand):
        vals = valuesOfHand(hand)
        #print(vals)
        t = 10
        for i in range(5):
            if t != vals[i]: return False
            t+=1
        return True
    return False


def straightFlush(hand):
    if isSameSuit(hand):
        vals = valuesOfHand(hand)
        #print(vals)
        
        for i in range(1,5):
            if vals[i] - vals[i-1] != 1: return False
            
        return True
    return False

def fourAKind(hand):
    vals = valuesOfHand(hand)
    freqs = frequency(vals)
    for i in range(1,15):
        if freqs[i] ==4:
            return True
    return False

def fullHouse(hand):
    vals = valuesOfHand(hand)
    freqs = frequency(vals)
    threeFlag = False
    pairFlag = False
    for i in range(1,15):
        if freqs[i] ==3:
            threeFlag = True
        if freqs[i] ==2:
            pairFlag = True
    if threeFlag and pairFlag:
        return True
    return False

def flushSuit(hand):
    suit = []
    for h in hand:
        suit.append(h[1])
    s = suit[0]
    for i in suit:
        if i != s:
            return False
    return True

def straight(hand):
    vals = valuesOfHand(hand)
    vals.sort()
    for i in range(4):
        if vals[i+1] - vals[i]!=1:
            return False
    return True

def ThreeKind(hand):
    vals = valuesOfHand(hand)
    freqs = frequency(vals)
    threeFlag = False

    for i in range(1,15):
        if freqs[i] ==3:
            return True
    return False

def twoPairs(hand):
    vals = valuesOfHand(hand)
    freqs = frequency(vals)
    countPair = 0
    for i in range(1,15):
        if freqs[i] ==2:
            countPair +=1
    
    if countPair ==2:
        return True
    return False

def aPair(hand):
    vals = valuesOfHand(hand)
    freqs = frequency(vals)
    for i in range(1,15):
        if freqs[i] ==2:
            return True
    return False

def highCard(hand):
    vals = valuesOfHand(hand)
    vals.sort()
    return vals[4]

def decision(hand):
    if(royalFlush(hand)): return 10
    elif straightFlush(hand): return 9
    elif fourAKind(hand):return 8
    elif fullHouse(hand):return 7
    elif flushSuit(hand):return 6
    elif straight(hand):return 5
    elif ThreeKind(hand):return 4
    elif twoPairs(hand) : return 3
    elif aPair(hand): return 2
    else: return 1

from collections import Counter
def highestPair(hand):
    vals = valuesOfHand(hand)
    valSet = set(vals)
    repeated = (Counter(vals) - Counter(valSet)).keys()
    highest = 0
    for i in repeated:

        if i > highest:
            highest = i
    return highest


totalGames = len(player1)


player1Wins = 0



for i in range(totalGames):
    pairCase1= False
    pairCase2 = False
    h1 = player1[i]
    h2 = player2[i]
    #print(h1,' ',h2)
    d1 = decision(h1)
    d2 = decision(h2)
    if d1 == 2 or d1 == 3 or d1 ==4 or d1 ==7 or d1==8: pairCase1 = True
    if d2 == 2 or d2 == 3 or d2 ==4 or d2 ==7 or d2==8: pairCase2 = True

    if d1 != d2:
        if d1>d2: player1Wins+=1
    else:
        if pairCase1 == False:
            c1= highCard(h1)
            c2 = highCard(h2)
            if c1>c2: player1Wins+=1
        else:
            hp1 = highestPair(h1)
            hp2 = highestPair(h2)
            if hp1>hp2: player1Wins+=1
            elif hp1 == hp2: 
                c1= highCard(h1)
                c2 = highCard(h2)
                if c1>c2: player1Wins+=1

    print(player1Wins)

