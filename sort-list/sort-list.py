# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        listClone = []
        while head!=None:
                listClone.append(head.val)
                head = head.next
        
        listClone.sort()
        head = None
        count = 0
        
        for nodeVal in listClone[::-1]:
            node = ListNode(nodeVal)
            node.next = head
            head = node
        
        return head