def combine(n, k):
    """
    Leetcode#77
    Given two integers n and k, return all possible combinations of k numbers chosen from the range [1,n].
    You may return the answer in any order.
    """
    def backtrack(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        for i in range(start, n + 1):
            curr.append(i)
            print("start:i:curr:result",start, i,curr, result)
            backtrack(i + 1, curr)
            curr.pop()
    result = []
    backtrack(1, [])
    return result

# Example usage
n = 4
k = 2
combinations = combine(n, k)
print(combinations)