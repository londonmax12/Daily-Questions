"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def TwoSum(nums, k):
    num_dict = {}
    for num in nums:
        num_dict[num] = True

        target = k - num
        if target in num_dict:
            return True
            
    return False

test_cases = [
    ([10, 15, 3, 7], 17),  # True, as 10 + 7 = 17
    ([1, 2, 3, 4, 5], 9),  # True, as 4 + 5 = 9
    ([2, 7, 11, 15], 9),   # True, as 2 + 7 = 9
    ([1, 2, 3, 4, 5], 10),  # True, as 5 + 5 = 10
    ([1, 2, 3, 4, 5], 20),  # False, no pair sums up to 20
    ([], 5),               # False, empty list has no pair
]

for nums, target in test_cases:
    result = TwoSum(nums, target)
    print(result)