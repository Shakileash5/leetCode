# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElementsTwo(self,head,val):
        headTemp = head
        prev = None
        
        while head:
            if head.val == val:
                if prev == None:
                    headTemp = head.next
                else:
                    prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return headTemp
        
    
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        def solutionOne():
            headTemp = head
            prev = None
            while(head!=None):
                flag = 0
                if head.val == val:
                    flag = 1
                    if head.next is not None:
                        head.val = head.next.val
                        head.next = head.next.next
                    else:
                        if prev == None:
                            headTemp = None
                            head = None
                        else:
                            prev.next = None
                            head = None
                        break

                if flag == 0:
                    prev = head
                    head = head.next

            return headTemp
        return self.removeElementsTwo(head,val)