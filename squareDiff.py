def fun(n):
    s1 = 0
    for i in range(1,n+1):
        s1 += i
    
    s1 = s1*s1

    s2 = 0
    for i in range(1,n+1):
        s2 += i*i
    
    diff = s1-s2
    return diff

print(fun(100))