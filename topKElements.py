import heapq
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
