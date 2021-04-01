# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fastPointer = head
        slowPointer = head
        visitedSet = set()
        
        while(slowPointer!=None and fastPointer!=None):
            
            if slowPointer in visitedSet:
                #print(slowPointer.val)
                return slowPointer
            visitedSet.add(slowPointer)
            slowPointer = slowPointer.next
            
            if fastPointer.next == None:
                return None
            fastPointer = fastPointer.next.next
            
            if slowPointer == fastPointer:
                #print(slowPointer.val)
                flag = 1
                #return True
        return None