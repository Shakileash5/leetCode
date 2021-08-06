# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        size = 0
        tempHead = head
        
        while tempHead:
            size += 1
            tempHead = tempHead.next
        if size == 0:
            return None
        k = k%size
        if k == 0 or k == size:
            return head
        
        nthNode = head
        prevNth = None
        tempNode = head
        idx = 1
        prev = None
        
        while(head):
            if idx>k:
                prevNth = nthNode
                nthNode = nthNode.next
            prev = head
            head = head.next
            idx += 1
            
        #print(prevNth,nthNode,prev)
        temp = nthNode
        prevNth.next = None
        head = nthNode
        prev.next = tempNode
        return head
        