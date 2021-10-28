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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode first = head, second = head, prev = null; 
        int idx = 1;
        
        if(head.next == null && n == 1){ // if only one node is present and need to be removed
            return null;
        }
        
        while(first.next != null){ // run till end of list
            if(idx >= n){ // if idx is greater than the nth idx then move the second idx along with first idx
                prev = second; // update prev if last node need to be removed
                second = second.next; 
            }    
            first = first.next;
            idx += 1;
        }
        
        if(second.next == null){ // if nth node is last node
            prev.next = null;
        }
        else if(idx == n){ // if 1st node need to be removed
            return head.next;
        }
        else{ // if node in middle need to be removed
            second.val = second.next.val;
            second.next = second.next.next;
        }
        return head;
        
    }
}