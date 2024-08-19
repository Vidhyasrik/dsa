def maxSubArray(nums):
    res = nums[0]
    total = 0
    resArr = list()
    for num in nums:
        if total<0:
            resArr.clear()
            total = 0
        total += num
        if total>res:
            resArr.append(num)
        res = max(res, total)
    return res

print("maxSub Array:=>", maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))