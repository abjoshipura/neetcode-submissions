import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = "".join(s.lower().split())
        print(s)
        return s[::-1] == s