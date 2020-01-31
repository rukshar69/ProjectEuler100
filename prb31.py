
ways = [[0 for i in range(8)] for j in range(201)]
ways1D = [ 0 for j in range(201)]
coins =  [1, 2, 5, 10, 20, 50, 100, 200]


def solution2D():

    for i in range(201):
        ways[i][0] = 1

    for i in range(0,201):

        for j in range(1,8):
            ways[i][j] = ways[i][j-1]

            if(coins[j]<=i):
                ways[i][j] += ways[i - coins[j]][j]

def solution1D():

    for i in range(201):
        ways1D[i]= 1
    
    for j in range(1,8):
        for i in range(201):
            ways1D[i] = ways1D[i]
            if coins[j] <= i: ways1D[i] += ways1D[i - coins[j]]

solution2D()
print(ways[200][7])

solution1D()
print(ways1D[200])

