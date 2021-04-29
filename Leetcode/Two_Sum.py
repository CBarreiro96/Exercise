"""
=================== Two Sum ==========================
------------------- Description ----------------------
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up
 to target.
You may assume that each input would have exactly one
solution, and you may not use the same element twice.
You can return the answer in any order.
"""


def twoSum(nums, target):
    Dictionary = {}
    for i, item in enumerate(nums):
        j = target - item
        if j not in Dictionary:
            Dictionary[item] = i
        else:
            return [Dictionary[j], i]


if __name__ == "__main__":
    print(twoSum([3, 2, 4], 6))
