# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        # take in the root of two trees and compare vaues 
        if a == None and b == None:
            return True
        elif a == None or b == None:
            return False
        elif a.val != b.val:
            return False
        
        left = self.isSameTree(a.left, b.left)
        right = self.isSameTree(a.right, b.right)

        return left and right # both must be true
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # compare root and subroot at each root's node
        if root == None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        left = self.isSubtree(root.left, subRoot) 
        right = self.isSubtree(root.right, subRoot)
        # subRoot is only one root and left and right, so just check root's left and right to it

        return left or right # as long as one tree is true, there is a match
        
