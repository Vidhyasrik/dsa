"""
LeetCode#344
Write a function that reverses a string. The input string is given as an array of characters s.
You must do thighs by modifying the input array in-place with O(1) extra memory.
"""
def reverseString(s):
    # return s[::-1]
    # return ''.join(reversed(s))
    if not s or len(s)<=1:
        return s
    low=0
    high=len(s)-1
    while low<high:
        s[low],s[high]=s[high],s[low]
        low +=1
        high -=1
    return s


print(reverseString(['N', 'a', 'g', 'i', 'R', 'e', 'd', 'd', 'y']))

