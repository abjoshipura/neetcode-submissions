import sys
class MinStack:
    def __init__(self):
        self.backing_array = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.backing_array.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        popped = self.backing_array.pop()
        if self.min_stack and popped == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.backing_array[-1]

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else -1
