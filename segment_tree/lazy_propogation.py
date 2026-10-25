# implementin lazy propogation in segment tree



arr=[5,6,1,2,9,6,2]
n=len(arr)
tree=[0]*(4*n)
lazy=[0]*(4*n)

def build(start,end,node):
    if start==end:
        tree[node]=arr[start]
        return
    mid=(start+end)//2
    build(start,mid,node*2+1)
    build(mid+1,end,node*2+2)
    tree[node]=tree[node*2+1]+tree[node*2+2]
build(0,n-1,0)
def push(start,end,node):
    if lazy[node]==0:
        return
    if start==end:
        lazy[node]=0
        return
    mid=(start+end)//2
    left=node*2+1
    right=node*2+2
    tree[left]+=(mid-start+1)*lazy[node]
    tree[right]+=(end-mid)*lazy[node]
    lazy[left]+=lazy[node]
    lazy[right]+=lazy[node]
    lazy[node]=0
def range_add(start,end,l,r,val,node):
    if l>end or r<start:
        return
    if l<=start and end<=r:
        tree[node]+=(end-start+1)*val
        if start!=end:
            lazy[node]+=val
        return
    push(start,end,node)
    mid=(start+end)//2
    range_add(start,mid,l,r,val,node*2+1)
    range_add(mid+1,end,l,r,val,node*2+2)
    tree[node]=tree[node*2+1]+tree[node*2+2]
def range_sum(start,end,l,r,node):
    if l>end or r<start:
        return 0
    if l<=start and end<=r:
        return tree[node]
    push(start,end,node)
    mid=(start+end)//2
    left=range_sum(start,mid,l,r,node*2+1)
    right=range_sum(mid+1,end,l,r,node*2+2)
    return left+right
print(tree)
range_add(0,n-1,2,5,6,0)
print(lazy,"\n",tree)
print(range_sum(0,n-1,2,4,0))
print(lazy)
print(tree)
print(range_sum(0,n-1,0,6,0))
print(lazy)
print(tree)