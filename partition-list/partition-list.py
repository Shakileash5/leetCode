# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        stackLessVal = []
        stackGreaterVal = []
        
        headC = head
        
        while head!=None:
            if head.val<x:
                stackLessVal.append(head.val)
            else:
                stackGreaterVal.append(head.val)
            
            head = head.next
        #print(stackGreaterVal,stackLessVal)
        head = headC
        while head!=None:
            if stackLessVal:
                head.val = stackLessVal.pop(0)
            else:
                head.val = stackGreaterVal.pop(0)
            
            head = head.next
        #print(headC)
        return headC