#minimum path sum

grid=[[5,1,8,2],[9,3,6,7],[2,1,8,3],[9,3,1,5],[9,9,2,1]]

n=len(grid)
m=len(grid[0])

for i in range(1,n):
    grid[i][0] += grid[i-1][0]


for i in range(1,m):
    grid[0][i] += grid[0][i-1]

for i in range(1,n):
    for j in range(1,m):
        if grid[i][j-1] < grid[i-1][j] :
            grid[i][j]+=grid[i][j-1]
        else:
            grid[i][j]+=grid[i-1][j]

print(grid[n-1][m-1])