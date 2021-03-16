# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        headC = head
        prev = None
        
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
            
            #print(flagC,"fl")
            if flagC == 1:
                
                #print(prev,start.next,head.val)
                if prev == None:
                    if start.next==None:
                        return prev
                        head.next = start.next
                        prev = head
                        
                    else:
                        #print("here")
                        head.next = start.next
                        headC = start.next
                else:
                    prev.next = start.next
                    #print("\nhey|",prev)
                    if start.next == None:
                        break
                    else:
                        head.next = start.next
                head = head.next
            else:
                #print("se",prev)
                if prev == None:
                    prev = head
                    headC = prev
                prev = head
                head = head.next
        
        #print(headC)
        return headC