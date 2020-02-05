

def solution(limit):
    erathosthenes = [True for i in range(1+limit)]
    erathosthenes[0] = False
    erathosthenes[1] = False

    for i in range(4,limit+1,2): erathosthenes[i] = False

    for i in range(3,limit+1,2):
        if erathosthenes[i]:
            for k in range(i*i, limit+1,i):
                erathosthenes[k] = False
        else:
            k = 1
            witness = False
            while k*k*2<i:
                if erathosthenes[ i - k*k*2] == True:
                    witness = True
                    break
                k+=1
            if witness==False: return i

print(solution(100000))

