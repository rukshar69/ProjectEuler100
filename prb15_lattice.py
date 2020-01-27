
def solutionDP(grid_dim):
    gridDP = [[0 for i in range(grid_dim+1)] for j in range(grid_dim+1)]
    gridDP[0][0] =1

    for i in range(grid_dim+1):

        for j in range(grid_dim+1):
            if i >0: gridDP[i][j] += gridDP[i-1][j]
            if j >0: gridDP[i][j] += gridDP[i][j-1]

    print(gridDP)
    
    return gridDP[grid_dim][grid_dim]

def solnCombinatorics(grid_dim):
    soln = 1
    for i in range(1,grid_dim+1):
        soln = (soln*(grid_dim+i))//i
    return soln

#print(solutionDP(2))
print(solnCombinatorics(20))