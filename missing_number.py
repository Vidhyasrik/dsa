# solution 1
def missingNumber(nums):
    n = len(nums) + 1
    v=[-1]*(n)
    for i in nums:
        v[i] = i
    for i in range(n):
        if v[i] == -1:
            return i
print(missingNumber([3,0,1]))

# solution 2(XOR Operation)
def missingNumber(nums):
    n=len(nums)
    ans=0
    for i in range(1,n+1):
        ans^=i
    for j in nums:
        ans^=j
    return ans

# solution 3
def missingNumber(nums):
    n = len(nums)
    Tsum=n*(n+1)/2
    return int(Tsum-sum(nums))

    
