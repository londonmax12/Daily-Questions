"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def ProductOfArray(nums):
    total_product = 1
    for num in nums:
        total_product *= num

    return [total_product // num for num in nums]

def ProductOfArrayNoDiv(nums):
    ret = []

    for index1, num1 in enumerate(nums):
        total = 1
        for index2, num2 in enumerate(nums):
            if index1 == index2:
                continue

            total *= num2
        ret.append(total)
    
    return ret
        
result = ProductOfArray([3, 2, 1])
print(result)