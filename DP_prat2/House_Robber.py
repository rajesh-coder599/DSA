# practice question

# recursion
# t=O(2^n)
# s=O(1)
arr=[5,3,1,8,6,2,9,4]

def rec(i,nums):
    if i>=len(nums):
        return 0

    take = nums[i]+ rec(i+2,nums)

    not_take=rec(i+1,nums)

    return max(take,not_take)

print(rec(0,arr))

# memorization
# t=O(n)
# s=O(n)
def memo(i,nums,dp):
    if i>=len(nums):
        return 0
    if dp[i]!=-1:
        return dp[i]
    take = nums[i]+ memo(i+2,nums,dp)

    not_take=memo(i+1,nums,dp)

    dp[i]=max(take,not_take)

    return dp[i]
n=len(arr)
dp=[-1]*n
print(memo(0,arr,dp))

# tabulation
# t=O(n)
# s=O(n)
def tab(i,nums,dp):
    n=len(nums)
    if n==1:
        return nums[0]
    dp[0]=nums[0]
    dp[1]=max(nums[0],nums[1])
    for i in range(2,n):
        take = nums[i] + dp[i-2]

        not_take=dp[i-1]

        dp[i]=max(take,not_take)

    return dp[n-1]
n=len(arr)
dp=[0]*n
print(tab(0,arr,dp))

# tabulation with space eficient
# t=O(n)
# s=O(1)
def tab(i,nums):
    n=len(nums)
    if n==1:
        return nums[0]
    a=nums[0]
    b=max(nums[0],nums[1])
    for i in range(2,n):
        take = nums[i] + a

        not_take=b

        c=max(take,not_take)
        a=b
        b=c

    return b
n=len(arr)
print(tab(0,arr))
