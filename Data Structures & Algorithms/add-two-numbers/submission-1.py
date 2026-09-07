# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Assume l1 is longer. If l1 is shorter, make the last node point to l2's first extra node

        head = l1
        prev = None

        carry = False
        while l1 and l2:
            digit_sum = l1.val + l2.val + carry
            l1.val = digit_sum % 10

            carry = digit_sum // 10

            prev = l1
            l1 = l1.next
            l2 = l2.next

        if l1 and not l2:
            while l1:
                digit_sum = l1.val + carry
                l1.val = digit_sum % 10
                carry = digit_sum // 10

                prev = l1
                l1 = l1.next

        elif not l1 and l2:
            prev.next = l2
            while l2:
                digit_sum = l2.val + carry
                l2.val = digit_sum % 10
                carry = digit_sum // 10

                prev = l2
                l2 = l2.next
        
        if carry:
            prev.next = ListNode(1, None)

        return head