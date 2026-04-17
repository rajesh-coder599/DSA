# boy or girl
s=input()
dic={}
n=0
for i in range(len(s)):
    if s[i] not in dic :
        n+=1
        dic[s[i]]=1

if n%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")