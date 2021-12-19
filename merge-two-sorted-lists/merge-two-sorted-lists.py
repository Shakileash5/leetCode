# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1,l2 = list1,list2 
        if l1 == None and l2 == None:
            return None
        if l1 == None and l2 != None:
            return l2
        if l2 == None and l1 != None:
            return l1
        
        if l1.val>l2.val:
            l1,l2 = l2,l1
        
        start1 = l1
        start2 = l2
        
        res = ListNode()
        temp = res
        prev = None
        
        while(start1 and start2):
            if start1.val < start2.val:
                res.val = start1.val
                start1 = start1.next
            else:
                res.val = start2.val
                start2 = start2.next
            prev = res
            res.next = ListNode()
            res = res.next
        
        while start1:
            res.val = start1.val
            res.next = ListNode()
            prev = res
            res = res.next
            start1 = start1.next
        
        while start2:
            res.val = start2.val
            res.next = ListNode()
            prev = res
            res = res.next
            start2 = start2.next
        
        prev.next = None
        return temp
        
        