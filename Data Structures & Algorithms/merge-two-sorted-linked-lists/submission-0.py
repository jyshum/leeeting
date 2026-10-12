# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        iterator1 = list1
        iterator2 = list2
        head = ListNode(0)
        curr = head

        while iterator1 and iterator2:
            if iterator1.val < iterator2.val:
                curr.next = iterator1
                iterator1 = iterator1.next
            else:
                curr.next = iterator2
                iterator2 = iterator2.next
            curr = curr.next
        curr.next = iterator1 or iterator2


        return head.next