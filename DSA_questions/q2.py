# parkour design
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    s=x+y
    if s>0 and s%3==0 and s/3>=abs(y):
        print("YES")
    else:        
        print("NO")