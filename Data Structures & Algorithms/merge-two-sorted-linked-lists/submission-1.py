# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0) # create a dummy node of "value = 0" since we need to build a new list from scratch
        curr = head # set the current to be the dummy node

        while list1 != None and list2 != None:
            # keep iterating through both lists as long as we havent reached their ends
            if list1.val < list2.val:
                # list1's node < list2's node, so we use list1's node
                curr.next = list1
                list1 = list1.next 
                # move list1 up since we dont want to check the same node on the next loop
            elif list2.val < list1.val:
                # list2's node < list1's node, so we use list2's node
                curr.next = list2
                list2 = list2.next 
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        
        if list1 != None:
            # list1 still has leftovers (happens when the lists have different lengths)
            curr.next = list1
        else:
            # list2 has leftovers
            curr.next = list2
        return head.next

