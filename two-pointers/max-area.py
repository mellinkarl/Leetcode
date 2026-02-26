"""
Name: Container With Most Water (11)
Difficulty: Medium
Mastered: Yes

Time: O(n)
Space: O(1)
Notes: Two pointer. Move pointer at shorter line.
"""
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = -1
        while left < right:

            # Current area is min between left and right's height * (right - left)
            min_height = min(heights[left], heights[right])
            max_water = max(max_water, min_height * (right - left))

            # Increment left if it's shorter, right otherwise
            if heights[left] == min_height:
                left += 1
            else:
                right -= 1

        return max_water

