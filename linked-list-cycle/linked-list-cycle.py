# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def findCycle(self,head):
        slow = head
        fast = head
        
        while slow and fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True
            
        return False
        
    
    def hasCycle(self, head: ListNode) -> bool:
        
        def solOne():
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
        
        return self.findCycle(head)