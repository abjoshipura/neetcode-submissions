from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        left = 0
        right = 0

        maxLength = 0
        while right < len(s):
            freq[s[right]] += 1

            while (right - left + 1) - sorted(freq.values(), reverse=True)[0] > k:
                freq[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

            right += 1
        
        return maxLength