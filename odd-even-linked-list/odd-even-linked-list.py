# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        tail = None
        end = None
        size = 0
        prev = None
        iseven = 0
        headTemp = head
        
        if head == None:
            return None
        
        while headTemp:
            if headTemp.next!=None:
                prev = headTemp
                end = headTemp.next
            
            if headTemp.next == None:
                size+=1
                end = headTemp
                break
            headTemp = headTemp.next.next
            size+=2
            
        
        if size%2==0:
            tail = end
            end = prev
            iseven = 1
            
        #print(tail,end,size)
        count = 1
        headTemp = head
        while(count<=((size-1)//2)):
            even = headTemp.next
            headTemp.next = headTemp.next.next
            end.next = even
            even.next = None
            #print(even,end,count)
            
            headTemp = headTemp.next
            end = end.next
            count+=1
        
        if iseven:
            end.next = tail
            tail.next = None
        #print(head)
        
        return head
        
        