"""
LeetCode#70
You are climbing a staircase that has n steps. You can either climb 1 step or 2 steps at a time. How many distinct ways can you climb to the top? Assume n>=1
"""
# Solution#1 Rescursive
def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climbStairs(n-1) + climbStairs(n-2)

# Solution#2# Dynamic Programming
def climb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
# Solution#3# Iterative
def climb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    prev, curr = 1, 2
    for i in range(3, n+1):
        temp = prev + curr
        prev = curr
        curr = temp
    return curr
#Test
for i in range(6):
    print(climb(i))  # Output: 1, 2, 3,

        
