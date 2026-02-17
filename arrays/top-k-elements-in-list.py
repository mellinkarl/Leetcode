"""
Name: Top K Frequent Elements (347)
Difficulty: Medium
Mastered: No

Time: O(n)
Space: O(n)
Notes: Count frequencies with a hashmap. Use bucket sort or a heap to retrieve the top k elements.
"""

from collections import Counter, heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(-val, key) for key, val in freq.items()]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
