import heapq
"""
LeetCode#347
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.
"""
import heapq

def topKFrequent(nums, k):
    """
    Finds the k most frequent elements in an array.

    LeetCode 347: Top K Frequent Elements

    Args:
        nums: A list of integers.
        k: The number of most frequent elements to return.

    Returns:
        A list of the k most frequent elements.
    """
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    heap =
    for num, frequency in frequency_map.items():
        heapq.heappush(heap, (-frequency, num))  # Use negative frequency for max-heap behavior

    result =
    for _ in range(k):
        result.append(heapq.heappop(heap))  # Extract the element (num)

    return result

# Alternative, more concise solution using collections.Counter and heapq.nlargest
import collections

def topKFrequent_concise(nums, k):
    """
    Finds the k most frequent elements using collections.Counter and heapq.nlargest.
    """
    counter = collections.Counter(nums)
    return [num for frequency, num in heapq.nlargest(k, ((frequency, num) for num, frequency in counter.items()))]

def topKElements(nums, k):
    heap = []
    counter = {}
    for num in nums:
        counter[num] = 1 + counter.get(num, 0)
    for k,v in counter.items():
        heapq.heappush(heap, (-v, k))
    res = []
    while len(res)<k:
        res.append(heapq.heappop(heap)[1])
    return res
