# Stones on the Table

n=int(input())
s=input()
prev=s[0]
if n==1:
    print(0)
else:
    ans=0
    for i in range(1,n):
        if s[i]==prev:
            ans+=1
        prev=s[i]
    print(ans)