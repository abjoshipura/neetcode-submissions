from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root):
            if not root:
                return None
            
            leftResult = inorderTraversal(root.left)
            if leftResult:
                return leftResult

            nonlocal k
            print(k, root.val)
            k -= 1
            if k == 0:
                return root.val

            rightResult = inorderTraversal(root.right)
            if rightResult:
                return rightResult
            
            return None
        
        return inorderTraversal(root)
            