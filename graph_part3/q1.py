# dijkstra's algorithm

## network delay time
import heapq
n=5
k=1
times=[(1,2,2),(1,3,1),(2,3,6),(2,4,3),(4,5,2)]

adj_list=[[]]*n

for i in times:
    x=i[0]
    y=i[1]
    z=i[2]

    adj_list[x-1].append([y,z])
    adj_list[y-1].append([x,z])

heap=[]
t=[float("inf")]*n
t[k-1]=0
heapq.heappush(heap,(t[k-1],k-1))

while len(heap)>0:
    a,b=heapq.heappop(heap)
    if a>t[b]:
        continue
    for i,j in adj_list[b] :
        if t[b]+j<t[i-1] :
            t[i-1]=t[b]+j
            heapq.heappush(heap,(t[i-1],i-1))

if max(t)==float("inf") :
    print(-1)
else:
    print(max(t))

