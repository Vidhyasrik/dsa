"""
LeetCode#238
Given an integer array, nums, return an array, products, such that product[i]is the product of all elements of nums except nums[i]
"""
def productExceptSelf1(nums):
    length = len(nums)
    products = [1] * length
    for i in range(1, length):
        products[i] = products[i - 1] * nums[i - 1]
    right_product = 1
    for i in range(length - 1, -1, -1):
        products[i] *= right_product
        right_product *= nums[i]
    return products

print("productExceptSelf1:=>", productExceptSelf1([2,3,4,5,6]))

# Solution#2
def productExceptSelf2(nums):
    length = len(nums)
    output = [1]*len(nums)
    left = 1
    right = 1
    for i in range(length):
        output[i] *= left
        left *= nums[i]
    for i in range(length-1, -1, -1):
        output[i] *= right
        right *= nums[i]
    return output
print("productExceptSelf2:=>", productExceptSelf2([2,3,4,5,6]))

# Solution#3
def productExceptSelf3(nums):
    n = len(nums)
    ans = [0]*n
    l=r=1
    l_product = [0]*n
    r_product = [0]*n
    for i in range(n):
        l_product[i] = l
        l*=nums[i]
    for i in range(n-1,-1,-1):
        r_product[i] = r
        r*=nums[i]

    for i in range(n):
        ans[i] = l_product[i]*r_product[i]
    return ans
print("productExceptSelf3:=>", productExceptSelf3([2,3,4,5,6]))


