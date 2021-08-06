# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        hashMap = {}
        
        while(head):
            if head in hashMap:
                return head
            hashMap[head] = 1
            head = head.next
        return None