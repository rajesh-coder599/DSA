#Q1
nums=[3,9,2,1,7]
k=3
freq={}
n=len(nums)
a=0
b=k-1
while b<n :
    sub_str=nums[a:b+1]
    for i in sub_str:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    b+=1
    a+=1
ans=[]
for k,v in freq.items() :
    if v==1 :
        ans.append(k)

if not ans :
    print(-1)
else:
    print(max(ans))

l=[]
l.append(1,2,3)