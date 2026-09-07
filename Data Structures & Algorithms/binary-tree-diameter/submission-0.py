# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def helper(root):
            if not root:
                return 0
            
            heightLeft = helper(root.left)
            heightRight = helper(root.right)

            nonlocal maxDiameter
            maxDiameter = max(maxDiameter, heightLeft + heightRight)

            return max(heightLeft, heightRight) + 1

        helper(root)

        return maxDiameter