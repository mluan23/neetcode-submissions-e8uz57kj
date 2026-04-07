# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        # get slow to the mid pt
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # now have to sort the end half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        prev # head of reversed

        while head:
            head_nxt = head.next
            prev_nxt = prev.next
            head.next = prev
            prev.next = head_nxt
            head = head_nxt
            prev = prev_nxt



        

        
        



# 0 -> 1 -> 2 -> 3 -> 4 -> 5
# can do 2 passes for O(n)    
# 0 -> x -> 1 -> x -> 2 -> x   