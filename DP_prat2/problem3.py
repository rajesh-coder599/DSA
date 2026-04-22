# longest pelindromic subsequence

# recursion
s1="abfcybza"
s2=s1[::-1]
n=len(s1)
def rec(i,j,s1,s2,n):
    if i>=n or j>=n :
        return 0
    
    if s1[i]==s2[j] :
        ans=1+rec(i+1,j+1,s1,s2,n)
    else:
        ans=max(rec(i+1,j,s1,s2,n),rec(i,j+1,s1,s2,n))

    return ans

print(rec(0,0,s1,s2,n))

# memorization

def memo(i,j,s1,s2,n,dp):
    if i>=n or j>=n :
        return 0
    
    if dp[i][j] != -1 :
        return dp[i][j]

    if s1[i]==s2[j] :
        dp[i][j]=1+memo(i+1,j+1,s1,s2,n,dp)
    else:
        dp[i][j]=max(memo(i+1,j,s1,s2,n,dp),memo(i,j+1,s1,s2,n,dp))

    return dp[i][j]

dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]
print(memo(0,0,s1,s2,n,dp))

# tabulation

def tab(s1,s2,n):
    dp=[[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1] :
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    return dp[n][n]

print(tab(s1,s2,n))

# tabulation with space optimization

def so(s1,s2,n):
    prev=[0]*(n+1)
    curr=[0]*(n+1)

    for i in range(1,n+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1] :
                curr[j]=1+curr[j-1]
            else:
                curr[j]=max(prev[j],curr[j-1])
        prev=curr[:]

    return curr[n]

print(so(s1,s2,n))