# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tempHead = head
        nthNode = head
        idx = 1
        prev = None
        while tempHead != None:
            #print(idx)
            if idx>n:
                prev = nthNode
                nthNode = nthNode.next
            tempHead = tempHead.next
            idx += 1
        if prev == None :
            return nthNode.next
        prev.next = prev.next.next
        #print(nthNode,prev)
        return head