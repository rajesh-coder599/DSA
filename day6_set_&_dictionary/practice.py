#Q1
#method1(brute method)
nums=[2,7,11,15]
target=9
ans=[]
for i in nums:
    for j in nums:
        if i+j==target:
            ans.append(nums.index(j))
            ans.append(nums.index(i))
        break
print(ans)
#method 2
ans2=[]
for i in range(len(nums)):
    second_number=target-nums[i]
    if second_number in nums:
        ans2.append(nums.index(second_number))
        ans.append(i)
print(ans2)
#method 3
dict1={}
for i in range(len(nums)):
    rem=target-nums[i]
    if rem in dict1:
        print([dict1[rem],i])
    else:
        dict1[nums[i]]=i

#Q1 part2(now we have sorted array)
nums=[1,2,3,4,5,6,7,8,9]
target=13
left=0
right=len(nums)-1
while left<right:
    sum1=nums[left]+nums[right]
    if sum1==target:
        print([left+1,right+1])
        break
    elif sum1>target:
        right-=1
    else:
        left+=1

#Q2 (intersection of two arrays with unique elements)
#method 1 without set
nums1=[1,2,3,4,1]
nums2=[3,4,1,1,5,6]
i = len(nums1)
j = len(nums2)
ans=[]
for k in range(min(i,j)):
    if nums1[k] in nums2 and nums1[k] not in ans:
        ans.append(nums1[k])
print(ans)
#method 2 with set
print(list(set(nums1)&set(nums2)))

#Q3 first unique charecter in a string
s="eetlcode"
dict1={}
for i in s:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]+=1
for key,value in dict1.items():
    if value ==1 :
        print(s.index(key))
        break

#Q4 valid anagram
#method 1
s="anagram"
t="nagaram"
a={}
b={}
for i in s:
    if i not in a:
        a[i]=1
    else:
        a[i]+=1
for i in t:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
print(a==b)

#Q5
s=["eat","tea","tan","ate","nat","bat"]
dict1={}
for i in s:
        s1=list(i)
        s1.sort()
        k="".join(s1)
        if k not in dict1:
            dict1[k]=[i]
        else:
            dict1[k].append(i)
print(dict1.values())

#Q6 (Distinct charechter)
s="aababcabc"
c=0
for i in range(len(s)-2):
    if(s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i]!=s[i+2]):
        c+=1
print(c)

#Q7 (longest distinct charechter length)
s="aababcdabc"
i=0
count=1
longest_distinct=1
for j in range(1,len(s)):
    longest_distinct=max(count,longest_distinct)
    if (s[j]!=s[i]):
        count+=1
    else:
        i=j
        count=1
print(longest_distinct)