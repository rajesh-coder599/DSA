## finding sum of specific range in an array using segment tree


a=[1,2,3,4,5,6,7,8,9,10]
n=len(a)
t=[0]*(4*n)
def build(arr,tree,node,start,end):
    if start==end:
        tree[node]=arr[start]
        return
    mid=(start+end)//2
    build(arr,tree,node*2+1,start,mid)
    build(arr,tree,node*2+2,mid+1,end)
    tree[node]=tree[node*2+1]+tree[node*2+2]
build(a,t,0,0,n-1)
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
update(t,0,0,n-1,-5,6)
print(t)
def range_sum(tree,node,start,end,l,r):
    if end<l or start>r:
        return 0
    if start>=l and end<=r:
        return tree[node]
    mid=(start+end)//2
    left=range_sum(tree,node*2+1,start,mid,l,r)
    right=range_sum(tree,node*2+2,mid+1,end,l,r)
    return left+right
print(range_sum(t,0,0,n-1,2,7))