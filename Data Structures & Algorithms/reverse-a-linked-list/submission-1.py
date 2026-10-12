# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # setting up the previous node as none (beginning of list) so that the current can point towards prev 
        cur = head # 0
        while cur != None:
            nxt = cur.next # save a copy since we will be changing cur.next, nxt of 0 is 1 [0 -> 1]
            cur.next = prev # flipping [None -> 0 -> 1] [0 -> None]
            prev = cur # prev turns from None to 0 to match the line above
            cur = nxt # cur is now 1
            # restart the loop, starting at 1, 1 will then point back to 0, prev becomes 1, cur will become 2 etc etc, so then prev eventually ends up as the first node after cur turns to None
        return prev # prev ends up at the front of the list, since it 

