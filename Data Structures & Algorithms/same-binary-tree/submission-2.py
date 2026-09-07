from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        pueue = deque()
        pueue.append(p)

        queue = deque()
        queue.append(q)

        while pueue and queue:
            node1 = pueue.popleft()
            node2 = queue.popleft()

            if (node1 is None and node2 is not None) or (node1 is not None and node2 is None):
                return False
            elif node1 is None and node2 is None:
                continue
            elif node1.val != node2.val:
                return False
            
            pueue.append(node1.left)
            pueue.append(node1.right)

            queue.append(node2.left)
            queue.append(node2.right)

        print(len(pueue))
        print(len(queue))

        return len(pueue) == len(queue)
