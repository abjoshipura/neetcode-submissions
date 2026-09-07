# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS from root till all nodes are covered.
        # Find the longest length
        if not root:
            return 0

        q = Queue()
        distances = defaultdict(lambda:-1)

        q.put(root)
        distances[root] = 0

        while not q.empty():
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            
            distances[node.left] = distances[node] + 1
            distances[node.right] = distances[node] + 1
        
        return max(distances.values())
