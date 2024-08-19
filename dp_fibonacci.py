# Solution:=>top down approach
def dp_fibo(n):
    dp=[-1]*(n+1)
    if n <= 1:
        return n
    if dp[n]==-1:
        dp[n]=dp_fibo(n-1)+dp_fibo(n-2)
        return dp[n]
    else:
        return dp[n]
# Solution:=> Bottom Up approach
def dp_fib(n):
    dp=[-1]*(n+1)
    dp[0:2]=0,1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
