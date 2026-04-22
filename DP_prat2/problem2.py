# longest common subsequence

text1="abefaghi"
text2="bfajeho"

def rec(i,j,text1,text2):
    if i>=len(text1) or j>=len(text2) :
        return 0
    
    if text1[i]==text2[j] :
        ans=1+rec(i+1,j+1,text1,text2)
    else:
        ans=max(rec(i+1,j,text1,text2),rec(i,j+1,text1,text2))

    return ans

print(rec(0,0,text1,text2))

# memorization

def memo(i,j,text1,text2,dp):
    if i>=len(text1) or j>=len(text2) :
        return 0
    if dp[i][j] != -1 :
        return dp[i][j]
    if text1[i]==text2[j] :
        dp[i][j]=1+memo(i+1,j+1,text1,text2,dp)
    else:
        dp[i][j]=max(memo(i+1,j,text1,text2,dp),memo(i,j+1,text1,text2,dp))

    return dp[i][j]

n=len(text1)
m=len(text2)
dp=[[-1 for i in range(m)] for j in range(n)]
print(memo(0,0,text1,text2,dp))

# tabulation

def tab(text1,text2,dp):
    
    for x in range(1,n+1):
        for y in range(1,m+1):
            if text1[x-1]==text2[y-1] :
                dp[x][y]=1+dp[x-1][y-1]
            else:
                dp[x][y]=max(dp[x-1][y],dp[x][y-1])
    return dp[n][m]

dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
print(tab(text1,text2,dp))

# tabulation with space optimization

def so(text1,text2):

    prev=[0]*(n+1)
    curr=[0]*(m+1)
    
    for x in range(1,n+1):
        for y in range(1,m+1):
            if text1[x-1]==text2[y-1] :
                curr[y]=1+prev[y-1]
            else:
                curr[y]=max(prev[y],curr[y-1])
        prev=curr[:]
    return curr[m]

print(so(text1,text2))