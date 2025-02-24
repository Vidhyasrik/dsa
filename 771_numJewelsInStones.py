"""
LeetCode#771
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a 
type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""
#Solution#1
def numJewelsInStones(jewels, stones):
    return sum(s in jewels for s in stones)  # count the number of stones
jewels, stones = "aA", "aAAbbbb"
print("Number Of Jewels in Stomes are:", numJewelsInStones(jewels, stones))
#solution#2
def numJewelsInStones(jewels, stones):
    count = 0
    for s in stones:
        if s in jewels:
            count +=1
    return count  # count the number of stones
print("Number Of Jewels in Stomes are:", numJewelsInStones(jewels, stones))