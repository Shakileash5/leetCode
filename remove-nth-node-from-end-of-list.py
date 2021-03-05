# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Problem Description

# Solution

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #print(head)
        if not head or not head.next:
            return None
        fastPointer = head
        nthPointer = head
        for i in range(0,n):
            fastPointer = fastPointer.next
        if not fastPointer:
            return nthPointer.next
        
        while fastPointer.next!=None:
            fastPointer = fastPointer.next
            nthPointer = nthPointer.next
        
        nthPointer.next = nthPointer.next.next
        return head
            