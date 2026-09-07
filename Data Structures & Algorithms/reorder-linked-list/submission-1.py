# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next
        
        slow.next = None

        temp = head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

        temp = prev
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

        newHead = head
        while head and prev:
            h_next = head.next
            head.next = prev

            p_next = prev.next
            prev.next = h_next

            head = h_next
            prev = p_next