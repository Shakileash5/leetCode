"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        hashMap = {}
        
        tempHead = head
        resHead = None
        
        while(tempHead):
            
            hashMap[tempHead] = Node(tempHead.val)
            if resHead == None:
                resHead = hashMap[tempHead] 
            tempHead = tempHead.next
        
        tempHead = head
        res = resHead
        
        while tempHead:
            if tempHead.next != None:
                resHead.next = hashMap[tempHead.next]
            else:
                resHead.next = None
            if tempHead.random != None:
                resHead.random = hashMap[tempHead.random]
            else:
                resHead.random = None
            #print(resHead.val,resHead.next.val)
            resHead = resHead.next
            tempHead = tempHead.next
        
        return res
            