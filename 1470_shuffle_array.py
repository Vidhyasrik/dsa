"""
LeetCode#1470
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

def shuffle(nums: list[int], n: int) -> list[int]:
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])
    return result

print(shuffle([1,2,3,4,5,6,7,8], 4))

# Method#2
def shuffle_concise(nums: list[int], n: int) -> list[int]:
    return [val for pair in zip(nums[:n], nums[n:]) for val in pair]

print(shuffle_concise([1,2,3,4,5,6,7,8], 4))