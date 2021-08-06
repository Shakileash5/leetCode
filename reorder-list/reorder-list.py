# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tempHead = head
        self.headMove = head
        size = [0]
        
        def recur(head,idx,prev):
            if head == None:
                size[0] = idx
                return 
            recur(head.next,idx+1,head)
            if idx>(size[0]//2):
                #print(self.headMove,head)
                next_ = self.headMove.next
                self.headMove.next = None
                self.headMove.next = head
                #print(self.headMove,head,next_)
                prev.next = None
                head.next = next_
                self.headMove = self.headMove.next.next
                #print(self.headMove,tempHead)
            return
        
        recur(head,0,None)
        #print(tempHead)
        return 1
            