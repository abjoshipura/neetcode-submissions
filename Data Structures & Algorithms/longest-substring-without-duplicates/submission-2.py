class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        maxLength = 0
        visitedChars = set()
        while right < len(s):
            if s[right] in visitedChars:
                while s[right] in visitedChars:
                    visitedChars.discard(s[left])
                    left += 1

            visitedChars.add(s[right])
            maxLength = max(maxLength, right - left + 1)
        
            right += 1
        
        return maxLength