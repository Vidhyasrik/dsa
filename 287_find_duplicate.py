def findDuplicate(nums):
    """
    Finds the duplicate number in an array where numbers are in the range [1, n].

    Args:
        nums: A list of integers.

    Returns:
        The duplicate number.
    """

    # Approach 1: Floyd's Cycle Detection (Tortoise and Hare)
    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow2 = 0
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]

    return slow

# Example Usage:
nums1 = [1, 3, 4, 2, 2]
print(findDuplicate(nums1))  # Output: 2

nums2 = [3, 1, 3, 4, 2]
print(findDuplicate(nums2))  # Output: 3

nums3 = [1,1]
print(findDuplicate(nums3)) #Output: 1

nums4 = [1,2,2]
print(findDuplicate(nums4)) #Output: 2

