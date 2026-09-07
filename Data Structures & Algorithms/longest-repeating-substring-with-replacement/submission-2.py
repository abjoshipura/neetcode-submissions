from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        maxLength = 0
        visitedChars = defaultdict(int)

        while right < len(s):
            visitedChars[s[right]] += 1
            
            while (right - left + 1) - sorted(visitedChars.values(), reverse=True)[0] > k:
                visitedChars[s[left]] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
            right += 1
        
        return maxLength