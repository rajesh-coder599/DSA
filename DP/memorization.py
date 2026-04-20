# Top down approach

# calculate fibonacci number


def fib(n,dp):
    if n==0 or n==1:
        return n
    
    if dp[n] != -1 :
        return dp[n]

    dp[n]=fib(n-1)+fib(n-2)
    
    return dp[n]

n=int(input())
dp=[-1]*(n+1)

print(fib(n,dp))
