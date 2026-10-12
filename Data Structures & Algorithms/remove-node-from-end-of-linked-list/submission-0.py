# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head # starts at node 1
        for _ in range(n):
            # most right forward n times so it creates the gap needed to remove the nth node
            right = right.next
        
        if right == None:
            # if right landed already landed the end of the list, it must mean the nth node is at the start of the list, so can just return the list starting from the second node
            return head.next 

        left = head
        while right.next != None:
            left = left.next
            right = right.next # move both pointers to mantain the gap 

        # right.next hits the end of the list, since the while loop above stopped
        left.next = left.next.next # make it so left skips the node in front of it since left's current node is the node right before 
        return head 

            