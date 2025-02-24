"""
LeetCode#509
The Fibonacci numbers, commonly denoted F(n) form a sequence, 
called the Fibonacci sequence, such that each number is the 
sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""
# Method - Top-Down Recursive
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Method - Top-Down Memoized
def fib(n):
    memo = {0: 0, 1: 1}
    if n in memo:
        return memo[n]
    if n <= 1:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
    memo[n] = result  # Store the result
    return result

# Bottom Up Constant Space
def fib(n) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        prev = 0
        cur = 1

        for i in range(2, n+1):
            prev, cur = cur, prev+cur
        
        return cur