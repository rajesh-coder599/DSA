# Q1 count number of conected component

n=8
edges=[(0,1),(1,5),(2,3),(2,6),(2,4),(3,4)]
adj_mat=[]
for i in range(n):
    adj_mat.append([-1]*n)
for i in edges:
    x=i[0]

    y=i[1]
    adj_mat[x][y]=1
    adj_mat[y][x]=1


visited=[False]*n

def dfs(i,visited,adj):
    visited[i]=True
    for x in range(n):
        if adj[i][x]==1 and visited[x]==False:
            dfs(x,visited,adj)

ans=0
for i in range(n):
    if not visited[i] :
        ans+=1
        dfs(i,visited,adj_mat)

print(ans)