"""
LeetCode#1137
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""

def tribonacci(n: int) -> int:
    t = [0,1,1]
    for i in range(3, n+1):
        t.append(t[i-1] + t[i-2] + t[i-3])
    return t[n] if n < len(t) else sum(t[-3:])
print(tribonacci(4))  # Output: 4
print(tribonacci(25))  # Output: 1389537
