"""
Name: Best Time to Buy and Sell Stock (121)
Difficulty: Easy
Mastered: Yes

Time: O(n)
Space: O(1)
Notes: Sliding window. Set left to right when price at right < price at left.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(len(prices)):
            # Check if current profit is higher than max
            max_profit = max(max_profit, prices[right] - prices[left])

            # If current price is less than lowest seen,
            # move left pointer to new low.
            if prices[right] < prices[left]:
                left = right
                
        return max_profit