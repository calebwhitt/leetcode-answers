# == https://leetcode.com/problems/two-sum/ ==

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for idx, num in enumerate(nums):
            match = target - num

            if match in dict:
                print([dict[match], idx])
            else:
                dict[num] = idx


# There is always only one pair that satisfy the condition. We can represent this algebraically such that 

# xa + xb = target                  therefore                     xa = target - xb

# So long as we keep a record of all previous values in the nums list, we can compare the current value to it's only pair

# ==================================================================================
# Runtime: 100 ms, faster than 63.24% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 24.20% of Python3 online submissions for Two Sum.
# ==================================================================================