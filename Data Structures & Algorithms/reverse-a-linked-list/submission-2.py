# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        tmp = head
        while head:
            tmp = head
            head = head.next
            tmp.next = prev
            prev = tmp
        return tmp
        

# 0>1>2>3
# 0 pts to 1, 1 to 2, 2 to 3
# tmp = 1
# head.next = 0
# head = 1
# tmp = 2
# head.next = 1
# head = 2