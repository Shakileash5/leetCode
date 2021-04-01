# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        sortedList = None
        
        headTemp = head
        
        
        def insert(node,head):
            if head == None:
                #print(node)
                return node
            prev = None
            headTemp = head
            while head!=None:
                if node.val<head.val:
                    if prev == None:
                        node.next = head
                        #print(node)
                        return node
                    else:
                        prev.next = node
                        node.next = head
                        #print(headTemp)
                        return headTemp
                prev = head
                head = head.next
            prev.next = node
            #print(headTemp)
            return headTemp
                        
        
        
        while head!=None:
            #print(head.val)
            node = ListNode(head.val)
            sortedList = insert(node,sortedList)
            head = head.next
        
        return sortedList