"""
LeetCode#46
Given an array nums of distinct integers, return all the possible 
permutations
. You can return the answer in any order.
"""
def permutation(nums):
    if len(nums)==1:
        return [nums[:]]
    res = []

    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permutation(nums)
        for p in perms:
            p.append(n)

        res.extend(perms)
        nums.append(n)

    return res

print(permutation([1,2,3]))

# Method#2
def permute(nums):
    """
    Generates all permutations of a list of distinct integers.

    LeetCode 46: Permutations

    Args:
        nums: A list of distinct integers.

    Returns:
        A list of lists, where each inner list is a permutation of nums.
    """
    if len(nums) == 0:
        return [[]]  # Base case: empty list has one permutation (empty list)

    if len(nums) == 1:
        return [nums[:]] # Base case: list of one element has one permutation

    result = []
    for i in range(len(nums)):
        first_element = nums[i]
        remaining_elements = nums[:i] + nums[i+1:]  # Create sublist without the first element
        sub_permutations = permute(remaining_elements)

        for sub_permutation in sub_permutations:
            result.append([first_element] + sub_permutation)

    return result

#Method#3
def permute_backtrack(nums):
    result = []
    def backtrack(index, current_permutation):
        if index == len(nums):
            result.append(current_permutation[:])
            return

        for i in range(len(nums)):
            if nums[i] not in current_permutation:
                current_permutation.append(nums[i])
                backtrack(index + 1, current_permutation)
                current_permutation.pop()

    backtrack(0, [])
    return result