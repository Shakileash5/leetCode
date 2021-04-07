# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        headTemp = head
        prev = None
        while(head!=None):
            flag = 0
            if head.val == val:
                #print(prev,head)
                if prev == None:
                    headTemp = head.next
                    flag = 1
                else:
                    prev.next = head.next
                    #print("\n",prev,"\n")
                    flag = 2
                    #head.next = None
            if flag == 1:
                prev = None
                head = head.next
            elif flag ==2:
                head = head.next
            else:
                prev = head
                head = head.next
        
        return headTemp