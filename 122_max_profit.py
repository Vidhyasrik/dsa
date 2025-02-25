"""
LeetCode#122
You are given an integer array prices where prices[i] 
is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
"""


def max_profit_ii(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:  # If the price is higher than the previous day
            max_profit += prices[i] - prices[i - 1]  # Add the profit to the total
    return max_profit
# Test the function
print(max_profit_ii([1, 2, 3, 4, 5]))
print(max_profit_ii([7, 1, 5, 3, 6]))