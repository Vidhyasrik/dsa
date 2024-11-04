"""
LeetCode#56
Given an array of intervals, where intervals[i]=[start, end], merge all overlapping intervals and return result
Ex:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""
def merge_intervals(intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals:
        # If the current interval overlaps with the last merged interval, merge them
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)
    return merged
# Test the function
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))  # Output: [[1,6],[8,10],[15,18]