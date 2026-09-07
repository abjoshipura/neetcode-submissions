class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        maxLength = 0
        visited_characters = set()
        while right < len(s):
            while s[right] in visited_characters:
                visited_characters.discard(s[left])
                left += 1

            visited_characters.add(s[right])
            
            maxLength = max(maxLength, right - left + 1)
            right += 1
        
        return maxLength