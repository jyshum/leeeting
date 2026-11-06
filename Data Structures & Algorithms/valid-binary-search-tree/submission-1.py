# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def searchLeft(node, lower, upper):
            if node is None:
                return True

            if lower is not None and node.val <= lower:
                return False

            if upper is not None and node.val >= upper:
                return False

            return (
                searchLeft(node.left, lower, node.val)
                and searchLeft(node.right, node.val, upper)
            )

        def searchRight(node, lower, upper):
            if node is None:
                return True

            if lower is not None and node.val <= lower:
                return False

            if upper is not None and node.val >= upper:
                return False

            return (
                searchRight(node.left, lower, node.val)
                and searchRight(node.right, node.val, upper)
            )

        leftResult = searchLeft(root.left, None, root.val)
        rightResult = searchRight(root.right, root.val, None)

        return leftResult and rightResult
         