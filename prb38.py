from itertools import permutations 
l = list(permutations(range(1, 10))) 


def concatPrd(numStr):
    for i in range(1,5):
        t = numStr[:i]
        #print('t :',t)
        s = t
        t_int = int(t)
        mult = 2
        while len(s)<9:
            tmep_t = mult*t_int
            #print('t_int :',t_int)
            s += str(tmep_t)
            mult+=1
        if numStr ==s:
            return True
    return False

limit = len(l)

def convertToStr(string):
    return "".join(map(str,string))

l.reverse()
for tup in l:
    #rint(convertToStr(tup))
    str_ = convertToStr(tup)
    if concatPrd(str_):
        print(str_)
        break

