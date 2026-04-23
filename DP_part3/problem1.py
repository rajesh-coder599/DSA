# longest increasing subsequence

nums=[10,9,2,5,3,7,101,18]
n=len(nums)
# recursion
def rec(nums,i,prev):
    if i==len(nums):
        return 0
    
    take=0
    if prev==-1 or nums[i]>nums[prev]:
        take=1+rec(nums,i+1,i)
    
    not_take=rec(nums,i+1,prev)

    return max(take,not_take)

print(rec(nums,0,-1))


# memorization
# t=O(n^2)
# s=O(n^2)
def memo(nums,i,prev,dp):
    if i==len(nums):
        return 0
    if dp[i][prev+1] != -1 :
        return dp[i][prev+1]
    take=0
    if prev==-1 or nums[i]>nums[prev]:
        take=1+memo(nums,i+1,i,dp)
    
    not_take=memo(nums,i+1,prev,dp)

    dp[i][prev+1]= max(take,not_take)
    return dp[i][prev+1]

dp=[[-1 for _ in range(n+1)] for _ in range(n)]
print(memo(nums,0,-1,dp))

# with lowerbond

def lowerbond(nums,target):
    n=len(nums)
    l=0
    r=n-1
    ans=n

    while l<=r:
        mid=(l+r)//2
        if nums[mid] >= target :
            ans=mid
            r=mid-1
        else:
            l=mid+1
    return ans

lis=[]
lis.append(nums[0])
for i in range(1,n):
    a=nums[i]
    if a>lis[-1] :
        lis.append(a)
    else:
        temp=lowerbond(lis,a)
        lis[temp]=a

print(len(lis))