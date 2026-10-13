# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        iterator1 = l1 # 1 -> 2 -> 3
        iterator2 = l2 # 4 -> 5 -> 6

        head = ListNode(0) # dummy
        cur = head
        carry = 0 # the extra 1 we pass to the next digit, starting at 0

        while iterator1 != None or iterator2 != None or carry != 0:
            # loop until all lists' ends are reached and carry finally equals 0

            # if this list still has a node, use its digit, otherwise use 0
            if iterator1 != None: 
                digit1 = iterator1.val 
            else:
                digit1 = 0
            if iterator2 != None:
                digit2 = iterator2.val
            else:
                digit2 = 0

            # add the two digits, plus the carry from the last column
            total = digit1 + digit2 + carry    

            # 10 or more means we carry a 1 to the next column, otherwise 0
            # example: total 15 gives carry 1
            carry = total // 10

            # the digit that stays in this column is the last digit of total
            # example: total 15 gives digit 5
            cur.next = ListNode(total % 10)  # make the new node and attach it
            cur = cur.next                   # move cur onto the new last node

            # move each iterator forward, but only if it isn't already None
            # (None.next would crash)
            if iterator1 != None:
                iterator1 = iterator1.next
            if iterator2 != None:
                iterator2 = iterator2.next

        return head.next # skip dummy node
        
