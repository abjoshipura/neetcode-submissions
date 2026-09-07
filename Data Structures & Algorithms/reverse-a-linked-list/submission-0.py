# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None

        currNode = head
        nextNode = currNode.next if currNode else None

        while currNode:
            currNode.next = newHead
            newHead = currNode

            currNode = nextNode
            nextNode = currNode.next if currNode else None

        return newHead
        # A -> B -> C -> D
        # B -> A