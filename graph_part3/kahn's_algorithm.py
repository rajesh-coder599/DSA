# topological sorting
from collections import deque
n=5
edge=[(0,1),(0,4),(0,3),(4,1),(4,3),(3,2)]

adj_list=[]
for i in range(n):
    adj_list.append([])
inorder=[0]*n
for i,j in edge:
    inorder[j]+=1
    adj_list[i].append(j)

ans=[]
q=deque()

for i in range(n):
    if inorder[i]==0:
        ans.append(i)
        q.append(i)

while len(q)>0:
    node=q.popleft()
    for x in adj_list[node]:
        inorder[x]-=1
        if inorder[x]==0:
            ans.append(x)
            q.append(x)

print(ans)