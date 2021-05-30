# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getPosition(self,head):
        tempHead = head
        count = 0
        visited = set()
        slow = head
        fast = head
        while slow and fast:
            if slow in visited:
                return slow
            visited.add(slow)
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return None
            
            
        
        
            
            
        
        
    def detectCycle(self, head: ListNode) -> ListNode:
        fastPointer = head
        slowPointer = head
        visitedSet = set()
        """
        while(slowPointer!=None and fastPointer!=None):
            
            if slowPointer in visitedSet:
                #print(slowPointer.val)
                return slowPointer
            visitedSet.add(slowPointer)
            slowPointer = slowPointer.next
            
            if fastPointer.next == None:
                return None
            fastPointer = fastPointer.next.next
            """
        return self.getPosition(head)