"""
Name: 3Sum (15)
Difficulty: Medium
Mastered: So-So

Time: O(n^2)
Space: O(n)
Notes: Sort + Two pointer. Skip duplicate first number at the beginning of the loop.
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        start = 0
        while start < len(nums) - 2 and nums[start] <= 0:
            left, right = start + 1, len(nums) - 1
            while left < right:
                curr_sum = nums[start] + nums[left] + nums[right]
                if curr_sum == 0:
                    res.add((nums[start], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
            start += 1
        return [list(triplet) for triplet in res]
                
