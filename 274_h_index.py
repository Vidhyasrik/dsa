"""
LeetCode#274
Given an array of integers citations where citations[i] is the number of 
citations a researcher received for their ith paper, return the researcher's 
h-index.According to the definition of h-index on Wikipedia: 
The h-index is defined 
as the maximum value of h such that the given researcher has published 
at least h papers that have each been cited at least h times.
"""


def h_index(citations):
    n = len(citations)
    citations.sort(reverse=True)
    h = 0
    for i in range(n):
        if citations[i] >= i + 1:
            h = i + 1
        else:
            break
    return h
# Test the function
print(h_index([3, 0, 6, 1, 5]))  #
# Output: 3
print(h_index([1, 3, 1]))  #
# Output: 1