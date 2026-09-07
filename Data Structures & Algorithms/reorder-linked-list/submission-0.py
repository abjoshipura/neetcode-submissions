# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math

class Solution:
    def printList(self, head: Optional[ListNode]) -> None:
        out = list()
        curr = head
        while curr:
            out.append(curr.val)
            curr = curr.next
        print(out)
    
    def reverseList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        # A -> B -> C -> D -> E -> F
        # A -> F -> B -> E -> C -> D

        length = 0
        length_curr = head
        while length_curr:
            length += 1
            length_curr = length_curr.next
        
        mid = length // 2
        midNode = head
        while mid:
            midNode = midNode.next
            mid -= 1
        
        reversed_curr = self.reverseList(midNode.next)
        midNode.next = None

        curr = head
        while curr and reversed_curr:
            nextNode = curr.next
            curr.next = reversed_curr
            reversed_curr = reversed_curr.next

            if curr.next:
                curr.next.next = nextNode

            curr = nextNode