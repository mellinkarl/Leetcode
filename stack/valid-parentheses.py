"""
Name: Valid Parentheses
Difficulty: Easy
Mastered: Yes

Time: O(n)
Space: O(n)
Notes: Stack
"""

class Solution:
    def isValid(self, s: str) -> bool:
        paren_pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in paren_pairs.keys():
                stack.append(c)
            else:
                if not stack or paren_pairs[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
        return True if not stack else False