"""
Name: Happy Number (202)
Difficulty: Easy
Mastered: No

Time: O(log n)
Space: O(1)
Notes: Repeatedly replace the number with the sum of the squares of its digits.
Use cycle detection (Floyd's algorithm) to determine if the sequence reaches 1 or enters a loop.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            
            # Convert n to sum of squares
            n_str = str(n)
            n = 0
            for c in n_str:
                n += int(c) ** 2
                
            # Hit cycle
            if n in seen:
                return False
            seen.add(n)
        
        # Got to 1
        return True