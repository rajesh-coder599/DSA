# DFS
n = 6 # number of nodes
e = 7 # number of edges

edges = [(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)]
adj=[]
for i in range(n):
    adj.append([])

for i in edges:
    x=i[0]
    y=i[1]

    adj[x].append(y)
    adj[y].append(x)

visited=[False]*n 
ans=[]
stack=[]

ans.append(0)
stack.append(0)
visited[0]=True

while len(stack) !=0:
    temp=stack.pop()
    for i in adj[temp]:
        if not visited[i] :
            stack.append(i)
            visited[i]=True
            ans.append(i)
print(ans)

# recursive traversal
visited=[False]*n
ans=[]
def dfs(i,visited,adj):
    visited[i]=True
    ans.append(i)
    for x in adj[i]:
        if not visited[x] :
            dfs(x,visited,adj)

dfs(0,visited,adj)
print(ans)