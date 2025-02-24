"""
LeetCode#1523
Given two non-negative integers low and high. 
Return the count of odd numbers between low and high (inclusive).
"""

def count_odds(low, high):
    length = high - low + 1
    count = length // 2
    if length % 2 and low % 2:
        count += 1
    return count



print(f"The Count of odd numbers:=>", count_odds(3,7))
print(f"The Count of odd numbers:=>", count_odds(4,7))
print(f"The Count of odd numbers:=>", count_odds(3,6))
print(f"The Count of odd numbers:=>", count_odds(4,8))