from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (not s and t) or (s and not t) or (len(s) != len(t)):
            return False

        charFrequencies = defaultdict(int)
        for char in s:
            charFrequencies[char] += 1
        
        for char in t:
            charFrequencies[char] -= 1
        
        for key in charFrequencies:
            if charFrequencies[key] != 0:
                return False
            
        return True