## how to build an segment tree

def build_segment_tree(arr,tree,node,start,end):
    if start==end:
        tree[node]=arr[start]
        return
    mid=(start+end)//2
    build_segment_tree(arr,tree,node*2,start,mid)
    build_segment_tree(arr,tree,node*2+1,mid+1,end)
    tree[node]=tree[node*2]+tree[node*2+1]

arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
tree=[0]*(4*n)
build_segment_tree(arr,tree,1,0,n-1)
print(tree)