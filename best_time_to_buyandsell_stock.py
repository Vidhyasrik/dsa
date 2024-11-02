"""
LeetCode#121
Given an array where the ith element is the price of a given stock on the  ith day, return the maximum profit achievable buying on one day ad sellig on another day in future
"""
# SOLUTION#1
def maxProfit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        profit = price - min_price
        max_profit=max(max_profit, profit)
        min_price = min(min_price, price)
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

# Solution#2
def maxProfit(prices):
    if not prices:
        return 0
    profit = 0
    buy = prices[0]
    for sell in prices:
        if sell>buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
