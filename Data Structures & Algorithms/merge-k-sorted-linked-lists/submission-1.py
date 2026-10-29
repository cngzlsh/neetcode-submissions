# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # let's use a heap
        if not lists: return None
        import heapq

        minHeap = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapq.heapify(minHeap)
        dummy = ListNode()
        tail = dummy
        while minHeap:
            _, i, node = heapq.heappop(minHeap)
            tail.next = node
            tail = tail.next
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))
        
        return dummy.next
