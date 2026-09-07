from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            else:
                if len(stack):
                    popped = stack.pop()
                    pair = (popped, char)
                    if pair not in (('(', ')'), ('{', '}'), ('[', ']')):
                        return False
                else:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True