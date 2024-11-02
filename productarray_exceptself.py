"""
LeetCode#238
Given an integer array, nums, return an array, products, such that product[i]is the product of all elements of nums except nums[i]
"""
def productExceptSelf(nums):
    length = len(nums)
    products = [1] * length
    for i in range(1, length):
        products[i] = products[i - 1] * nums[i - 1]
    right_product = 1
    for i in range(length - 1, -1, -1):
        products[i] *= right_product
        right_product *= nums[i]
    return products

print("productExceptSelf:=>", productExceptSelf([2,3,4,5,6]))