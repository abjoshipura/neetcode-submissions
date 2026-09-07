class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        left = 0
        right = 1

        max_length = 1
        while left < right:
            visited = dict()
            visited[s[left]] = left

            while right < len(s) and s[right] not in visited:
                visited[s[right]] = right
                right += 1
            
            # right is either len(s) or the index of the first repetition
            print(left, right)
            max_length = max(max_length, right - left)

            if right == len(s):
                break
            else:
                # skip left to the index right after the earliest index of the repeated letter
                left = visited[s[right]] + 1
                right = left + 1

        return max_length