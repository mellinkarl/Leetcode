"""
Name: Encode and Decode String (271)
Difficulty: Medium
Mastered: Yes

Time: O(n)
Space: O(n + m), where n is total characters in given strings & m is total number of words
Notes: Delimit at START, not end.
"""

from collections import Counter, heapq
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            # Start each word with "{word_len}!"
            encoded.append(str(len(word)) + "!")
            encoded.append(word)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        words = []
        i, j = 0, 0
        while i < len(s):

            # Get word_len
            while s[j] != "!":
                j += 1
            curr_word_len = int(s[i:j])

            # Get actual word
            i = j + 1
            j = i + curr_word_len
            words.append(s[i:j])
            i = j

        return words
