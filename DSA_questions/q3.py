# Course Wishes
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    level=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    ans_arr=[]

    freq=[0]*(k+2)
    for x in arr:
        freq[x]+=1
    possible=True
    for i in range(1,k+1):
        if freq[i]>level[i-1]:
            possible=False
    if not possible:
        print(-1)
        continue
    moved=True

    while moved:
        moved=False

        for i in range(n-1,-1,-1):
            x=arr[i]
            while x<k+1:
                if x==k:
                    ans_arr.append(i+1)
                    arr[i]+=1
                    x+=1
                    moved=True
                elif x<k and arr.count(x+1)<level[x]:
                    arr[i]+=1
                    ans_arr.append(i+1)
                    x+=1
                    moved=True
                else:
                    break
    print(len(ans_arr))
    print(*ans_arr)

    
                