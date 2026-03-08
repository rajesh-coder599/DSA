#counting sort
nums=[3,2,8,1,7,6,4]
freq=[0]*(max(nums)+1)
print(freq)
for i in nums:
    freq[i]+=1
nums.clear()
for i in range(len(freq)):
    while freq[i]>0:
        nums.append(i)
        freq[i]-=1
print(nums)
