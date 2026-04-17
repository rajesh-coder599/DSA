# find cycle

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
def hascycle(i,parent,adj,visited):
    visited[i]=True

    for x in adj[i]:
        if x==parent:
            continue
        if visited[x] :
            return True
        if hascycle(x,i,adj,visited) :
            return True
    return False

print(hascycle(0,-1,adj,visited))