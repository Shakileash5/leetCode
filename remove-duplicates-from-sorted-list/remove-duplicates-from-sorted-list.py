# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        headC = head
        if head == None:
            return head
        while head.next!=None:
            flagC = 0
            if head.next!=None and head.val == head.next.val:
                start = head
                flagC = 1
                end = head.next
                flag = 0
                while start.val == end.val:
                    if end.next==None:
                        flag = 1
                        break
                    temp = end
                    end = end.next
                
                if flag == 0:
                    start.next = end
                else:
                    start.next = None
            
            if flagC == 1:
                head = start
            else:
                head = head.next
        
        print(headC)
        return headC
                
                    
                