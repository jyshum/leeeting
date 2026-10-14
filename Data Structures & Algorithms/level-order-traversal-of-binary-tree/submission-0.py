# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = [] # set up array as the result

        queue = collections.deque()
        queue.append(root)
        
        while queue: # as long as its not empty
            queueLength = len(queue) # set up the length, to run through elements within the level
            level = [] # set up the array of each level to add to queue
            
            for i in range(queueLength): # looping through the queue
                # taking the node from the queue, as that is the parent node for the children below
                node = queue.popleft() 
                if node != None:
                    level.append(node.val) # append the parent node to the queue first
                    queue.append(node.left) # then append the childrens to the queue; can be iterated through next loop
                    queue.append(node.right)
            if level: # as long as its not empty
         # add in the level to output only if it isnt null, since some levels can be empty like the bottom of each branch
                output.append(level) 
        
        return output