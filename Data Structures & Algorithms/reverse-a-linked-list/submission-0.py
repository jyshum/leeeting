# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur != None:
            nxt = cur.next
            cur.next = prev # flipping it [0,1], prev is none and next is 1, next turns into none
            prev = cur # 
            cur = nxt
        return prev

