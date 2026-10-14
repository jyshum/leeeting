# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None: # if node is null, go back to original node
            return
        copy = root.left # save original left root, as the current left root will be changed
        root.left = root.right # set left root to right root
        root.right = copy # set right root to left root

        self.invertTree(root.left) # recursively do the same for the left children nodes
        self.invertTree(root.right) # once left side is done by return, do the same for the right
        return root # once both left and right are done, return root