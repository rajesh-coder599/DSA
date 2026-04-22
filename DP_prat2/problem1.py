# Partition equal subset sum

arr=[8,1,4,5,3,3]

def partition(i,arr,sum1,total):
    if len(arr)==1:
        return False
    if total%2 != 0:
        return False
    
    if sum1>total//2:
        return False
    elif sum1==total//2:
        return True    
    elif i==len(arr):
        return False
    take=partition(i+1,arr,sum1+arr[i],total)
    not_take=partition(i+1,arr,sum1,total)

    return take or not_take

total=sum(arr)
ans=partition(0,arr,0,total)
print(ans)

# memorization

def memo(i,arr,sum1,total,dp):
    if len(arr)==1:
        return False
    if total%2 != 0:
        return False
    
    if sum1>total//2:
        return False
    elif sum1==total//2:
        return True    
    elif i==len(arr):
        return False
    if dp[i][sum1] != -1 :
        return dp[i][sum1]
    take=memo(i+1,arr,sum1+arr[i],total,dp)
    not_take=memo(i+1,arr,sum1,total,dp)

    dp[i][sum1] = take or not_take
    return dp[i][sum1]

total=sum(arr)
n=len(arr)
dp=[[-1 for i in range(total//2+1)] for j in range(n)]
ans=memo(0,arr,0,total,dp)
print(ans)