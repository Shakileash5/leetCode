# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        headATemp = headA
        nodeStackA = []
        nodeStackB = []
        
        while headA!=None or headB!=None:
            if headA == headB:
                return headA
            if headA !=None:
                #if headA.next!=None:
                if hasattr(headA,'checked'):
                    return headA 
                headA.checked = True
                headA = headA.next
            if headB != None:
                if hasattr(headB,'checked'):
                    return headB 
                #nodeStackB.append(headB)
                headB.checked = True
                headB = headB.next
            #elif countB == 0:
            #    nodeStackB.append(headB)
                
        
        
        return None