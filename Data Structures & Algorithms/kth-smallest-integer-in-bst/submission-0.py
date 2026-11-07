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
        #   2. make list into ascending order
        #   3. loop through the array by k and return k index value in the list

        data = []

        def dfs(node):
            if node == None:
                return
            
            data.append(node.val)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        data.sort()
        return data[k-1]
