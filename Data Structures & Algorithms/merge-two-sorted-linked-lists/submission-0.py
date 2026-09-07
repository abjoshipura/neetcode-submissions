# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None

        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    head = list1
                    tail = list1
                else:
                    tail.next = list1
                    tail = tail.next
                list1 = list1.next
            else:
                if not head:
                    head = list2
                    tail = list2
                else:
                    tail.next = list2
                    tail = tail.next
                list2 = list2.next
        
        while list1:
            if not head:
                head = list1
                break
            else:
                tail.next = list1
                list1 = list1.next
                tail = tail.next

        while list2:
            if not head:
                head = list2
                break
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next

        return head
