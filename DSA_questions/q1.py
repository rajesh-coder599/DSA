# all of these questions from codeforsec round 1091(Div.2)

## Q1 Flip the Bit (Easy Version)

t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    x=int(input()) - 1
    right=0
    if arr[n-1] != arr[x] :
        right = 1
    for i in range(x+1,n):
        if arr[i] != arr[i-1] :
            right +=1
    
    left=0
    if arr[0] != arr[x] :
        left =1
    for i in range(x-1,-1,-1):
        if arr[i] != arr[i+1] :
            left +=1
    
    print("ans:",max(right,left))
