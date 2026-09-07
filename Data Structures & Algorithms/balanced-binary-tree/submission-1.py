# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True

        def get_height(root):
            if not root:
                return 0
            if not root.left and not root.right: 
                return 1

            return max(get_height(root.left), get_height(root.right)) + 1

        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        left_height = get_height(root.left)
        right_height = get_height(root.right)

        if abs(left_height - right_height) > 1:
            return False
        else:
            return True