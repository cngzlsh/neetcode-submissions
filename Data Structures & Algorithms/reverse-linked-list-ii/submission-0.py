# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next              # node just before the segment

        curr = prev.next                  # first node of the segment
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next          # unlink nxt
            nxt.next = prev.next          # put nxt at the front of the segment
            prev.next = nxt
        return dummy.next

            
