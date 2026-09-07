class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = dict()
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for char in t:
            if char in freq:
                freq[char] -= 1
            else:
                return False
        
        flag = False
        for char in freq:
            flag = (flag or freq[char])
        
        return not flag