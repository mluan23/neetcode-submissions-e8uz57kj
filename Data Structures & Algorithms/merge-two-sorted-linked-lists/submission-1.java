/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode iter = dummy;
        if(list1 == null){
            return list2;
        }
        if(list2 == null){
            return list1;
        }
        while(list1 != null && list2 != null){
            if(list1.val < list2.val){
                iter.next = list1;
                list1 = list1.next;
            }
            else{
                iter.next = list2;
                list2 = list2.next;
            }
            iter = iter.next;
            
        }
        if(list1 == null){
                iter.next = list2;
                list2 = list2.next;
            }
            else{
                iter.next = list1;
                list1 = list1.next;
            }
        return dummy.next;
    }
}