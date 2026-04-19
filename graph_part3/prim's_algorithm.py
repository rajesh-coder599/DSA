# minimum spaning tree
import heapq
n=5
edge=[(0,1,9),(0,2,75),(1,2,95),(1,3,19),(1,4,42),(2,3,51),(2,4,66),(3,4,31)]
adj_list=[]
for i in range(n):
    adj_list.append([])
for i,j,k in edge:
    adj_list[i].append([j,k])
    adj_list[j].append([i,k])

visited=[False]*n
visited[0]=True
ans=0
for _ in range(n-1):
    mn=float("inf")
    temp=-1
    for i in range(n):
        if visited[i]:
            for node,weight in adj_list[i]:
                if not visited[node] and weight<mn:
                    mn=weight
                    temp=node

    if temp==-1:
        break
    ans+=mn
    visited[temp]=True

print(ans)

## with heap

visited=[False]*n
heap=[]
heapq.heappush(heap,(0,0))
ans=0
while len(heap)>0:
    weight,node=heapq.heappop(heap)

    if visited[node]:
        continue
    visited[node]=True
    ans+=weight
    for nei,w in adj_list[node]:
        if not visited[nei]:
            heapq.heappush(heap,(w,nei))

print(ans)