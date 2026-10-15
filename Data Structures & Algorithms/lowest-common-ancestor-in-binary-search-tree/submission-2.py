# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we can look for a "split" between p and q, since this is a BST
        cur = root 

        while cur != None:
            if p.val < cur.val and q.val < cur.val: 
                # both values are smaller, meaning both are in the left branch
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                # both values are greater, maning both are in right branch
                cur = cur.right
            else:
                # other conditions, meaning that there is a split
                return cur