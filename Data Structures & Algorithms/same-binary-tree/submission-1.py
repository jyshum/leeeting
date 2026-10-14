# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # iterate through both trees p and q and keep track if each left and right are equal

        # handle both none case; if both are none, the trees are matching
        if p == None and q == None:
            return True
        # handle one none case; if one case is none, the trees are mismatching
        elif p == None or q == None:
            return False
        # compare values,
        elif p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left) # iterate left side
        right = self.isSameTree(p.right, q.right) # iterate right side
        
        return left and right # both have to be true
        