# alternating string

t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    dic={"a":0,
         "b":0}
    for i in range(1,n):
        if s[i]==s[i-1]:
            dic[s[i]]+=1

    if dic["a"]==dic["b"] and dic["a"]<2:
        print("YES")
    elif dic["a"] != dic["b"] :
        if dic["a"]==0 and dic["b"]<=2:
            print("YES")
        elif dic["b"]==0 and dic["a"]<=2 :
            print("YES")
        else:
            print("NO")
    else:
        print("NO")