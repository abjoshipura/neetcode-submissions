# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = None, head

        while fast and n > 0:
            fast = fast.next
            n -= 1
        
        if not fast:
            if not slow:
                return head.next
            else:
                return None
        else:
            while fast:
                if not slow:
                    slow = head
                else:
                    slow = slow.next

                fast = fast.next

            slow.next = slow.next.next
            return head