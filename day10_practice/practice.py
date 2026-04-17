#Q1 koko eating banana
piles=[12,7,8,9,5,3,10]
h=8
n=len(piles)
l=1
r=max(piles)
k=r
while l<=r :
    mid=(l+r)//2
    ans=0
    for i in piles:
        ans+=(i+mid-1)//mid
    if ans>h :
        l=mid+1
    else:
        k=mid
        r=mid-1
print(k)

#Q2 search in 2D matrix(if not then find correct position)
num=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=22
row=len(num)
col=len(num[0])
l=0
r=row*col-1
ans=[]
while l<=r :
    mid=(l+r)//2
    if num[mid//col][mid%col] <= target :
        l=mid+1
        ans.clear()
        ans.append(mid//col)
        ans.append(mid%col)
    else :
        r=mid-1
print("at",ans)

#Q3
nums=[3,1,2,4]
l=0
r=len(nums)-1
while l<=r :
    if nums[l]%2 != 0 and nums[r]%2 ==0 :
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
    elif nums[l]%2 == 0 and nums[r]%2 !=0 :
        l+=1
        r-=1
    elif nums[l]%2 == 0 :
        l+=1
    else:
        r-=1
print(nums)