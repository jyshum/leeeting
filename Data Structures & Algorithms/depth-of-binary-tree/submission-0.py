# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # keep track every time we call a maxDepth
        if root == None: # node is null, stop recursive call
            return 0
        left = self.maxDepth(root.left) # call recursively on left for LEFT VARIABLE
        right = self.maxDepth(root.right) # call recursively on right for RIGHT VARIABLE
        return 1 + max(left,right) # once, both the left and right subtree depts are found for that one node, return 1 is the node on its own so it can keep adding until it finds 0 for that specific node