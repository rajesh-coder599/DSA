# THU Packing Puzzle
t=int(input())
for i in range(t):
    t,h,u=map(int,input().split())
    ans=0
    if u!=0 and t!=0:
        if t<=u:
            a=u-t+h
            ans+=(t*4+a*3)
        else:
            if h==0:
                ans+=(u*4+t*3)

            else:
                ans+=(u*4)
                t-=u
                if t>=2*h:
                    b=t-2*h
                    ans+=(h*7+t*3)
                else:
                    if t%2==0:
                        c=h-t//2
                        ans+=((h-c)*7+(c*3))
                    else:
                        t-=1
                        c=h-t//2
                        ans+=((h-c)*7+(c*3)+2)
    elif t==0 and h==0 and u==0:
        ans=0
    elif u==0 and h==0:
        l=t-1
        ans+=(t*3-l)
    elif t==0:
        k=h+u
        ans+=(k*3)
    elif u==0:
        if t>=2*h:
            b=t-2*h
            ans+=(h*7+t*3)
        else:
            if t%2==0:
                c=h-t//2
                ans+=((h-c)*7+(c*3))
            else:
                t-=1
                c=h-t//2
                ans+=((h-c)*7+(c*3)+2)
    
    print(ans)