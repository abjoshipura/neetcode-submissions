from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Null Input
        # Empty String
        # Does whitespace count?

        # Iterate over each string
        # Keep track of each string's character's frequencies.

        # If the two frequencies match, then they are anagrams
        # Early exit if there is a mismatch

        if not s or not t or len(s) != len(t):
            return False
        
        s_charFrequencies = defaultdict(int)
        for char in s:
            s_charFrequencies[char] += 1

        t_charFrequencies = defaultdict(int)
        for char in t:
            t_charFrequencies[char] += 1
        
        for key in s_charFrequencies:
            if key not in t_charFrequencies or s_charFrequencies[key] != t_charFrequencies[key]:
                return False
        
        return True