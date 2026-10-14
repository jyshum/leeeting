# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        
        rootLeft = root.left # save original left root, as the current left root will be changed
        root.left = root.right # set left root to right root
        root.right = rootLeft # set right root to left root

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root