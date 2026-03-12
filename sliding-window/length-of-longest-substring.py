"""
Name: Length of Longest Subtstring
Difficulty: Medium
Mastered: Yes

Time: O(n)
Space: O(m), where m is the number of unique chars.
Notes: Sliding window. Move left when encounter duplicate.
"""
from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen = set()
        for right in range(len(s)):
            if s[right] in seen:
                while s[left] != s[right] and left < right:
                    seen.remove(s[left])
                    left += 1
                left += 1
            longest = max(longest, right - left + 1)
            seen.add(s[right])
        return longest
            
