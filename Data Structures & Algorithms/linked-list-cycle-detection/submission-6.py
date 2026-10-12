# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # since we're not given the index as a parameter, how do we know its a cycle if we cant assume that the list isnt just a normal list with the same repeating sequence like 1 2 3 2 3 2 3...
        # USE A HASHSET containing the all the visited nodes
        seen = set()

        cur = head
        if cur == None:
            return False
        while cur != None:
            seen.add(cur)
            cur = cur.next
            if cur == None:
                return False
            elif cur in seen:
                return True
