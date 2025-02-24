"""
LeetCode#202
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

def isHappy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1
print(isHappy(19)) # True
print(isHappy(20)) # False
print(isHappy(1)) # True
print(isHappy(7)) # True
print(isHappy(4)) # False