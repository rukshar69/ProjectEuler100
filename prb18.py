fname = 'number.txt'
f = open(fname,'r')

f1 = f.readlines()
#print(f1)
nums = []
for line in f1:
    line = line.split(' ')
    #print(line)
    line = [int(a) for a in line]
    #print(line)
    nums.append(line)

limit = len(nums)
#print(limit)
solution = []
def recursive(i,j,prd):
    if i>=limit:
        solution.append(prd)
        return
    
    recursive(i+1,j,nums[i][j]+prd)
    recursive(i+1,j+1,nums[i][j]+prd)

#recursive(0,0,0)
#print(max(solution))

def dp(triangle, n):
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
    
    return triangle[0][0]

print(dp(nums,limit))
    
    