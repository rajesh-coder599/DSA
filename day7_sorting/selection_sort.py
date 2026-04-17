# selection sort
nums=[3,2,8,1,7,6,4]
for i in range(len(nums)):
    min1=nums[i]
    ind=i
    for j in range(i+1,len(nums)):
        if(nums[j]<min1):
            min1=nums[j]
            ind=j
    temp=nums[ind]
    nums[ind]=nums[i]
    nums[i]=temp
print(nums)