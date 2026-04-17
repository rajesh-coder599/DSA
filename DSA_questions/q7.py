# Helpful Maths

s=input()
if len(s)==1:
    print(s)
else:
    a=s.split("+")
    a.sort()
    ans="+".join(a)
    print(ans)