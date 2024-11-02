"""
LeetCode#322
Given an integer array coins, representing coins of different denominations, and an integer amount, return the fewest number of coins that you need to make up that amount. If it is impossible to make that amount, return -1. Assume you have an infinite number of coins
"""
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

print("Coins", coinChange([1,2,4], 4))

