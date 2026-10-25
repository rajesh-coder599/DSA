## val update in segment tree

def build(arr,tree,node,start,end):
    if start==end:
        tree[node]=arr[start]
        return
    mid=(start+end)//2
    build(arr,tree,node*2+1,start,mid)
    build(arr,tree,node*2+2,mid+1,end)
    tree[node]=tree[node*2+1]+tree[node*2+2]
arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
t=[0]*(4*n)
build(arr,t,0,0,n-1)
print(t)
def update(tree,node,start,end,val,idx):
    if start==end:
        tree[node]=val
        return
    mid=(start+end)//2
    if idx<=mid:
        update(tree,node*2+1,start,mid,val,idx)
    else:
        update(tree,node*2+2,mid+1,end,val,idx)
    tree[node]=tree[node*2+1]+tree[node*2+2]
update(t,0,0,n-1,6,8)
print(t)