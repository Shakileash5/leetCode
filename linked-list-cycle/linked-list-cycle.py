# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        fastPointer = head
        slowPointer = head
        
        while(slowPointer!=None and fastPointer!=None):
            
            slowPointer = slowPointer.next
            if fastPointer.next == None:
                return False
            fastPointer = fastPointer.next.next
            
            if slowPointer == fastPointer:
                return True
        return False