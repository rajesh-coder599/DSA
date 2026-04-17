#BFS

#adjacency list

from collections import deque
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
q=deque()

ans.append(0)
q.append(0)
visited[0]=True

while len(q) !=0:
    temp=q.popleft()
    for i in adj[temp]:
        if not visited[i] :
            q.append(i)
            visited[i]=True
            ans.append(i)

print(ans)


