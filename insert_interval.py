"""
LeetCode#57
insert Interval

"""

def insert(intervals, newInterval):
    result = []
    i = 0
    while(i<len(intervals) and intervals[i][1]<newInterval[0]):
        result.append(intervals[i])
        i+=1
    while(i<len(intervals) and intervals[i][0]<=newInterval[1]):
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i+=1
    result.append(newInterval)
    """
    while i<len(intervals):
      result.append(intervals[i])
      i+=1
    """
    result += intervals[i:]
    return result
