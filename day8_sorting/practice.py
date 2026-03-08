#Q1 (sort colors)
#0,1,2 respectivly red,white and blue
nums=[2,0,2,1,1,0]
l=0
r=len(nums)-1
k=0
while k<=r:
    if nums[k]==0 :
        nums[l],nums[k]=nums[k],nums[l]
        k+=1
        l+=1
    elif nums[k]==2 :
        nums[k],nums[r]=nums[r],nums[l]
        r-=1
    elif nums[l]==1:
        k+=1
print(nums)
#counting sort method
nums=[2,0,2,1,1,0]
n=[0]*((max(nums))+1)
for i in nums:
    n[i]+=1
nums.clear()
for i in range(len(n)):
    while n[i]>0:
        nums.append(i)
        n[i]-=1
print(nums)

#Q2 (merge sorted array)
#input
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
#solve
i=m-1
j=n-1
k=m+n-1
while j>=0:
    if nums1[i]<=nums2[j] :
        nums1[k]=nums2[j]
        k-=1
        j-=1
    elif nums1[i]>nums2[j] :
        nums1[k],nums1[i]=nums1[i],nums1[k]
        i-=1
        k-=1
print(nums1)

#Q3 non overlaping intervals
intervals=[[1,2],[2,3],[3,4],[1,3]]
intervals.sort(key=lambda x: x[1])
n=len(intervals)

a=0
c=1
for i in range(1,n):
    if intervals[i][0]>=intervals[a][1]:
        a=i
        c+=1
print(n-c)