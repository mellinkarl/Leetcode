"""
Name: Valid Sudoku (36)
Difficulty: Medium
Mastered: So-So

Time: O(n^2)
Space: O(n^2)
Notes: Can do it in O(n) space if using hashset for the squares.
"""

from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for r in range(len(board)):
            curr_set = set()
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in curr_set:
                    return False
                curr_set.add(board[r][c])
        
        # Check columns
        for c in range(len(board[0])):
            curr_set = set()
            for r in range(len(board)):
                if board[r][c] == '.':
                    continue
                if board[r][c] in curr_set:
                    return False
                curr_set.add(board[r][c])
        
        # Check boxes
        box_freq = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                curr_box = (r // 3, c // 3)
                if board[r][c] in box_freq[curr_box]:
                    return False
                box_freq[curr_box].add(board[r][c])
        return True
