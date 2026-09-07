# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if not root:
        #     return None
        
        # # If p and q are both on one side, then I am not the ancestor and I move to that side
        # # If p and q are on opposite sides, then I am the ancestor
        # # I could be either p or q, in which case, I am the ancestor

        # if p == root or q == root:
        #     return root

        # if p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # if p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        
        # return root

        # If I am p or q, I return myself to the parent
        # On receiving: p => forward p to parent
        # q => forward q to parent
        # p and q: forward myself to the parent

        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root

        leftReturn = self.lowestCommonAncestor(root.left, p, q)
        rightReturn = self.lowestCommonAncestor(root.right, p, q)

        if leftReturn and rightReturn:
            return root
        elif leftReturn:
            return leftReturn
        elif rightReturn:
            return rightReturn
        else:
            return None