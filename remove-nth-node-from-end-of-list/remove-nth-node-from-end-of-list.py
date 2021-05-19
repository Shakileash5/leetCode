# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solutionTwo(self,head,n):
        prev = None
        tempHead = head
        nthNode = head
        count = 0
        while head!=None:
            if count>=n:
                prev = nthNode
                nthNode = nthNode.next
            count+=1
            head = head.next
        #print(nthNode.val)
        if prev != None:
            prev.next = nthNode.next
        else:
            tempHead = tempHead.next
        
        return tempHead 
        
        
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #print(head)
        def solutionOne():
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
        
        return self.solutionTwo(head,n)
            