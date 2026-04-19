# Antimedian Deletion

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if n<3:
        x=[n]*n
        print(*x)
    else:
        print([2]*n) 