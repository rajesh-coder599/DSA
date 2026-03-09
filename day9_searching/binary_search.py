#binary search this is only aplicable in sorted array O(logn)
nums=[1,2,3,4,5,6,7,8,9]
target=7
n=len(nums)
l=0
r=n-1
while l<=r :
    mid=(l+r)//2
    if nums[mid]>target :
        r=mid-1
    elif nums[mid]<target :
        l=mid+1
    else:
        print(mid)
        break

#lower bound
nums1=[1,3,7,9,11,12,21,32,44]
target=10
n=len(nums1)
l=0
r=n-1
ans=n
while l<=r :
    mid = (l+r)//2
    if target>nums1[mid] :
        l=mid+1
    else:
        r=mid-1
        ans=mid
print(ans)

#upper bound
nums1=[1,3,7,9,11,12,21,32,44]
target=10
n=len(nums1)
l=0
r=n-1
ans=n
while l<=r :
    mid = (l+r)//2
    if target>=nums1[mid] :
        l=mid+1
    else:
        r=mid-1
        ans=mid
print(ans)