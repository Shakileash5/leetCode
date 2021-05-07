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
                flag = 1
                while(head.val == val):
                    if head.next is not None:
                        #prev = head
                        head.val = head.next.val
                        head.next = head.next.next
                    else:
                        #print("here",head)
                        if prev == None:
                            headTemp = None
                            head = None
                            #print("here2",headTemp,head)
                            break
                        else:
                            prev.next = None
                            head = None
                            break
            if flag == 0:
                prev = head
                head = head.next
        
        return headTemp