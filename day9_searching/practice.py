#Q1 (find first and last position of element in sorted array)
nums=[5,7,7,8,8,10]
target=8
n=len(nums)
l=0
r=n-1
first_position=0
while l<=r :
    mid=(l+r)//2
    if target>nums[mid] :
        l=mid+1
    else:
        r=mid-1
        first_position = mid
l=0
r=n-1
last_position=0
while l<=r :
    mid=(l+r)//2
    if target>=nums[mid] :
        l=mid+1
    else:
        r=mid-1
        last_position=mid
ans=[first_position,last_position-1]
print(ans)

#Q2 (peak of the mountain array)
arr=[2,4,5,8,12,14,1]
n=len(arr)
l=0
r=n-1
while l<=r :
    mid = (l+r)//2
    if arr[mid-1]<=arr[mid]>=arr[mid+1] :
        l=mid
        break
    elif arr[mid+1]<=arr[mid]<=arr[mid-1] :
        r=mid-1
    elif arr[mid+1]>=arr[mid]>=arr[mid-1] :
        l=mid+1
    
print(l)

#Q3 (square root of x)
x=65
l=0
r=x
ans=1
while l<=r:
    mid=(l+r)//2
    mid_sqr=mid*mid
    if mid_sqr>x :
        r=mid-1
    else:
        ans=mid
        l=mid+1
print(ans)