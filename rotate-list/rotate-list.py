# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        size = 0
        if k == 0 or head == None:
            return head
        temp = head
        while(temp):
            temp = temp.next
            size += 1
        
        if size == 1:
            return head
        
        k = k%size
        
        nthNode = head
        temp = head
        count = 0
        prev = None
        lastNode = None
        
        while(temp and k):
            if count >= k:
                prev = nthNode
                nthNode = nthNode.next
            lastNode = temp
            temp = temp.next
            count += 1
        
        if prev == None:
            return head
        
        #print(nthNode.val,prev.val,lastNode.val)
        prev.next = None
        lastNode.next = head
        head = nthNode
        return head
        