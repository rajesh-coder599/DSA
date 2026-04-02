# graph repersentation
n = 6 # number of nodes
e = 7 # number of edges

edges = [(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)]

# adjacency list
adj=[]
for i in range(n):
    adj.append([])

for i in edges:
    x=i[0]
    y=i[1]

    adj[x].append(y)
    adj[y].append(x)

for i in adj:
    print(i)

# adjacency matrix
adj_mat=[]
for i in range(n):
    adj_mat.append([-1]*n)

for i in edges:
    x=i[0]
    y=i[1]

    adj_mat[x][y]=1
    adj_mat[y][x]=1

for i in adj_mat:
    print(i)