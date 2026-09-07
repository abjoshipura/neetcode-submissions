from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False
        
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1
        
        for char in t:
            freq_map[char] -= 1
        
        return not any(freq_map.values())