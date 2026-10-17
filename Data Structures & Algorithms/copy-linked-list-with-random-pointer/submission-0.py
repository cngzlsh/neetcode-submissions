"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        clonehead = Node(head.val)
        clonecurr, origcurr = clonehead, head
        orig2clone = {None:None}
        orig2clone[origcurr] = clonecurr

        while origcurr.next:
            origcurr = origcurr.next
            clonecurr.next = Node(origcurr.val)
            clonecurr = clonecurr.next
            orig2clone[origcurr] = clonecurr
        
        clonecurr, origcurr = clonehead, head
        while clonecurr:
            clonecurr.random = orig2clone[origcurr.random]
            clonecurr = clonecurr.next
            origcurr = origcurr.next

        return clonehead 

        
        

