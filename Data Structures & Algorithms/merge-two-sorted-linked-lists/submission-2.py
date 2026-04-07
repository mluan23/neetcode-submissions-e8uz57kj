# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head
        # so traverse as long as one of them has stuff
        while list1 or list2:
            # empty list1, so add the rest of list2
            if not list1:
                head.next = list2
                head = head.next
                list2 = list2.next
            elif not list2:
                head.next = list1
                head = head.next
                list1 = list1.next
            else:   # both lists have stuff
                if list1.val <= list2.val:
                    head.next = list1
                    head = head.next
                    list1 = list1.next
                else:
                    head.next = list2
                    head = head.next
                    list2 = list2.next
        return dummy.next
