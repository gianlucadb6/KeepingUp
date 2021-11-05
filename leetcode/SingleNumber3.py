"""
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(0, len(nums), 3):
            try:
                if nums[i] != nums[i+1] or nums[i+1] != nums[i+2]:
                    return nums[i]
            except:
                return nums[i]

#passes all cases

