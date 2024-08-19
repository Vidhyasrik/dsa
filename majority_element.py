#   Solution-1
# def majorityElement(nums):
#     hash = {}
#     res = majority = 0
#     for num in nums:
#         hash[num] = hash.get(num, 0) + 1
#         if hash[num] > majority:
#             majority = hash[num]
#             res = num
#     return res
# Time complexity = O(n)
# Space complexity = O(n)

#   Solution-2
def majorityElement(nums):
    res = majority = 0
    for n in nums:
        if majority == 0:
            res = n
        majority += 1 if n==res else -1
    return res

nums=[1,1,2,2,1,1]
print(majorityElement(nums)) # Output: 1