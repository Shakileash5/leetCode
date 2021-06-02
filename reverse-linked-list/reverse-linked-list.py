# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recur(self,head,parent,revHead):
        if head == None:
            revHead = parent
            return revHead
        revHead = self.recur(head.next,head,revHead)
        head.next = parent
        return revHead
    
    def reverseList(self, head: ListNode) -> ListNode:
        def reverseIterative():
            prev = None
            current =  head
            if current == None:
                return None
            next = head.next

            while(current!=None):
                next = current.next
                current.next = prev
                prev = current
                current = next

            return prev
        
        return self.recur(head,None,None)
        
        