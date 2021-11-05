"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        for i in range(0, len(nums), 2):
            try:
                if nums[i] != nums[i + 1]:
                    return nums[i]
            except:
                return nums[i]

#passes all test cases
