from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS and count distance
        if not root:
            return 0
        
        queue = deque()
        queue.appendleft(root)

        distances = dict()
        distances[root] = 1

        while len(queue):
            node = queue.pop()

            if node.left:
                queue.append(node.left)
                distances[node.left] = distances[node] + 1
            if node.right:
                queue.append(node.right)
                distances[node.right] = distances[node] + 1
        
        return max(distances.values())
            

