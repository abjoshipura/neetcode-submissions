# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Empty SLLs
        # Single Elements
        # Self References
        # Duplicates

        def printSLL(head: ListNode):
            while head:
                print(head.val, end=" ")
                head = head.next
            print()

        if not list1:
            return list2
        if not list2:
            return list1
        
        dummy = ListNode(0, list1)
        prev1 = dummy
        curr1 = list1

        curr2 = list2

        while curr1 and curr2:
            if curr2.val <= curr1.val:
                prev1.next = curr2

                next2 = curr2.next
                curr2.next = curr1

                prev1 = prev1.next
                curr2 = next2
            else:
                prev1 = curr1
                curr1 = curr1.next
        
        printSLL(dummy.next)
        
        while curr2:
            prev1.next = curr2
            prev1 = prev1.next

            curr2 = curr2.next

        return dummy.next
            
            