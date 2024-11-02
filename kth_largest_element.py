"""
A Heap is a complete binary tree data structure that satisfies the heap property: for every node, the value of its children is greater than or equal to its own value. 
"""
import heapq
def findKthlargest(nums: list[int], k: int)->int:
    heap = []
    for i in range(k):
        heap.append(nums[i])
    heapq.heapify(heap)
    for i in range(k,len(nums)):
        if nums[i] > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,nums[i])
    return heap[0]

print("The kthlargest element in Array is:=>", findKthlargest([2,1,9,5,7,3,6], 3))