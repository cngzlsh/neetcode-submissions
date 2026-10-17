# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2:

            l1n = l1.val if l1 else 0
            l2n = l2.val if l2 else 0
            
            curr.next = ListNode(val = (l1n + l2n + carry) % 10)
            if l1n + l2n + carry >= 10:
                carry = 1
            else:
                carry = 0

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry: # e.g. 1 + 999
            curr.next = ListNode(1)
        
        return dummy.next