# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # stop. think about it.
        # ok so how do you reverse a linked list
        # keep track of the previous element
        # make it so that your next element, it points to that previous element
        # and that's it
        # then increment the head to the next element
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

