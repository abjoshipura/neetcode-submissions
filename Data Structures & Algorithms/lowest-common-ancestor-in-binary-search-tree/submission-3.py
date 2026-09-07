# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if root.val == p.val:
            return p
        if root.val == q.val:
            return q

        leftResult = self.lowestCommonAncestor(root.left, p, q)
        rightResult = self.lowestCommonAncestor(root.right, p, q)

        if leftResult and rightResult:
            return root
        elif leftResult and not rightResult:
            return leftResult
        elif rightResult and not leftResult:
            return rightResult
        else:
            return None

        