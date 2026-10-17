# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: 
            return

        fast, slow = head, head
        # start fast and slow pointers, fast reach end, slow in the middle
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse second half
        curr, prev = slow.next, None
        slow.next = None
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        second = prev # head of reversed half

        first = head
        
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        

        
        