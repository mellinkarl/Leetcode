"""
Name: Product of Array Except Self (238)
Difficulty: Medium
Mastered: Yes

Time: O(n)
Space: O(n)
Notes: Prefix & Suffix sum
"""

from collections import Counter, heapq
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # Get prefix sum
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # Get suffix sum
        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        # Multiply prefix and suffix sum for each element
        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        return res
