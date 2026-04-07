# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        amt = length - n
        if amt == 0:
            return head.next
        dummy = head
        for i in range(length - 1):
            if (i + 1) == amt:
                dummy.next = dummy.next.next
                break
            dummy = dummy.next
        return head

        return dummy
        



        
        
        
        