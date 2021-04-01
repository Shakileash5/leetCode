# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        reverseList = []
        headTemp = head
        
        while head!=None:
            reverseList.append(head)
            head = head.next
        
        reverseList = reverseList[::-1]
        
        head = headTemp
        
        while head!=None:
            
            tempNext = head.next
            if tempNext not in reverseList:
                head.next = None
                break
            head.next = reverseList.pop(0)
            head = head.next
            head.next = tempNext
            
            head = head.next
        return 
            