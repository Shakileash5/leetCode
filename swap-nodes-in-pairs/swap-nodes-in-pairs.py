# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        curr = head
        count = 0
        
        while curr!= None:
            if curr.next:
                val = curr.next.val
                curr.next.val = curr.val
                curr.val = val
                curr = curr.next.next
            else:
                break
        """while curr.next!=None:
            if count%2==0: 
                print("here")
                temp = curr.next.val
                curr.next.val = curr.val
                curr.val = temp
            curr = curr.next
            count+=1"""
            
        
        return head
           