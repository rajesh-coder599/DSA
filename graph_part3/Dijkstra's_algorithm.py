# shortest path algorithm
import heapq
n=6
e=8
edge=[(0,2,4),(0,1,4),(1,2,2),(2,3,3),(2,5,6),(2,4,1),(3,5,2),(5,4,3)]
adj_list=[]
for i in range(n):
    adj_list.append([]*n)

for i in edge:
    x=i[0]
    y=i[1]
    z=i[2]

    adj_list[x].append([y,z])
    adj_list[y].append([x,z])

heap=[]
dis=[float("inf")]*n
dis[0]=0
heapq.heappush(heap,(dis[0],0))
while len(heap)>0:
    d,v=heapq.heappop(heap)
    if d>dis[v]:
        continue
    for i,j in adj_list[v]:
        if dis[v]+j <dis[i]:
            dis[i]=dis[v]+j
            heapq.heappush(heap,(dis[i],i))

print(dis)