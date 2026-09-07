from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        
        freq_s1 = defaultdict(int)
        for char in s1:
            freq_s1[char] += 1

        freq_s2 = defaultdict(int)
        left = 0
        right = left + len(s1) - 1
        for i in range(left, right):
            freq_s2[s2[i]] += 1

        while right < len(s2):
            freq_s2[s2[right]] += 1

            if freq_s1.items() <= freq_s2.items():
                return True

            if s2[left] in freq_s2:
                freq_s2[s2[left]] -= 1
                if freq_s2[s2[left]] == 0:
                    del freq_s2[s2[left]]
            
            left += 1
            right += 1
        
        return False