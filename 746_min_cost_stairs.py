"""
LeetCode#746
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor
"""

def min_cost_climbing_stairs(cost):
    n = len(cost)
    dp = [0] * (n+1)
    dp[0] = cost[0] if n > 0 else 0
    dp[1] = cost[1] if n > 1 else (cost[0] if n > 0 else 0)
    for i in range(2, n+1):
        if i < n:
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        else:
            dp[i] = min(dp[i - 1], dp[i - 2])
    return dp[n]

# Method#2
def min_cost_climbing_stairs(cost):
    n = len(cost)
    cost.append(0)
    for i in range(n - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    return min(cost[0], cost[1])

# Method#3
def min_cost_climbing_stairs(cost):
    n = len(cost)
    cost.append(0)
    for i in range(n - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    return min(cost[0], cost[1])

#Method#4
def min_cost_climbing_stairs(cost):
    n = len(cost)
    dp = [0] * n
    dp[0] = cost[0] if n > 0 else 0
    dp[1] = cost[1] if n > 1 else (cost[0] if n > 0 else 0)
    for i in range(2, n+1):
        if i < n:
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        else:
            dp[i] = min(dp[i - 1], dp[i - 2])
    return min(dp[-1], dp[-2])