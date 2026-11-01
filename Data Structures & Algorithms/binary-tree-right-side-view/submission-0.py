# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def dfs(node, depth):
            if node == None:
                return

            if len(output) == depth:
                # This is the first node visited at this depth.
                # Since we explore right before left, it is the
                # rightmost node at this level.
                output.append(node.val)

            # Explore both subtrees, visiting the right one first.
            # Other nodes at an already-recorded depth won't be added.
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)  # The root is at depth 0.
        return output
