from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque()
        queue.append((root, 0))
        
        levelOrder = []
        while queue:
            node, level = queue.popleft()
        
            if len(levelOrder) == level:
                levelOrder.append([])
            levelOrder[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        output = []
        for level in levelOrder:
            output.append(level[-1])
        
        return output