# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # idea:
        #   1. iterate through BST and add every node value to a list 
        #   2. make sure values are addded in order from left to right since this is a BST (left is smaller than right) "inorder traversal"
        #   3. loop through the array by k and return k index value in the list

        data = []

        def dfs(node):
            if node == None:
                return

            dfs(node.left)
            data.append(node.val) #
            dfs(node.right)

        dfs(root)
        return data[k-1]
