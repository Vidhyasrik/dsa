"""
LeetCode#1071
For two strings s and t, we say "t divides s" if and only 
if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, 
return the largest string x such that x divides both str1 and str2.
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def gcd_of_strings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    common_length = gcd(len(str1), len(str2))
    return str1[:common_length]
print(gcd_of_strings("ABCABC","ABC"))  # "ABC"  # Output: