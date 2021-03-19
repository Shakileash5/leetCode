# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        
        currentNode = head
        start = head
        currentPosition = 1
        
        while currentPosition < left:
            start = currentNode
            currentNode = currentNode.next
            currentPosition += 1
        tail = currentNode
        reversedLinkedList = None
        while currentPosition >= left and currentPosition <= right:
            nxt = currentNode.next
            currentNode.next = reversedLinkedList
            reversedLinkedList = currentNode
            currentNode = nxt
            currentPosition += 1
        
        start.next = reversedLinkedList
        tail.next = currentNode
        
        if left >1:
            return head
        else:
            return reversedLinkedList
        
        
        
            
        