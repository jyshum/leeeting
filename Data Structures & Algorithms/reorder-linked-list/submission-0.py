# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle, and reverse the second half and then join both halfs

        # to find the middle, use slow & fast pointers

        if head == None or head.next == None:
            return
        
        slow = head
        fast = head

        while fast != None and fast.next != None: 
            slow = slow.next
            fast = fast.next.next

        currentR = slow.next 
        slow.next = None # split halfs
        prev = None 

        while currentR != None:
            nxt = currentR.next
            currentR.next = prev
            prev = currentR
            currentR = nxt
        
        first = head
        second = prev

        while second != None:
            nextFirst = first.next
            nextSecond = second.next

            first.next = second
            second.next = nextFirst
            # first -> second -> nextFirst

            first = nextFirst
            second = nextSecond
            # move both nodes
        
            


        




