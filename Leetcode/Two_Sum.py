'''
=================== Two Sum ==========================
------------------- Description ----------------------
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up
 to target.
You may assume that each input would have exactly one
solution, and you may not use the same element twice.
You can return the answer in any order.
'''
def twoSum(nums, target):
    a = []
    for i, item in enumerate(nums):
        k = i
        for j in nums[i + 1:]:
            k += 1
            if item + j == target:
                a.append(i)
                a.append(k)
    return a


if __name__ == "__main__":
    print(twoSum([3, 2, 4], 6))
