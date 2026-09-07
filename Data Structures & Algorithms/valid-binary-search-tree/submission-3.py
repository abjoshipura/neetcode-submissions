# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def helper(root):
            if not root:
                return (1001, -1001)
            
            leftOutput = helper(root.left)
            if leftOutput:
                leftMin, leftMax = leftOutput
            else:
                return None

            rightOutput = helper(root.right)
            if rightOutput:
                rightMin, rightMax = rightOutput
            else:
                return None

            if leftMax >= root.val:
                return None
            if rightMin <= root.val:
                return None
            
            return (min(leftMin, rightMin, root.val), max(leftMax, rightMax, root.val))
        
        return helper(root) is not None

