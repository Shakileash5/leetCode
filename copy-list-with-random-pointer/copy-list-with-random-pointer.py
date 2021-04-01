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
        
        hashList = {}
        
        headTemp = head
        copyList = []
        count = 0
        while(head!=None):
            node = Node(head.val)
            copyList.append(node)
            head.copyIdx = count
            count+=1
            head = head.next
        
        head = headTemp
        size = len(copyList)
        cloneHead = None 
        count = 0
        
        while head!=None:
            cloneNode = copyList[count]
            if count==0:
                cloneHead = cloneNode
            if count+1<size:
                cloneNode.next = copyList[count+1]
            else:
                cloneNode.next = None
            
            if head.random == None:
                cloneNode.random = None
            else: 
                cloneNode.random = copyList[head.random.copyIdx]
            head = head.next
            count+=1
            
            
        
        
        
        #print(copyList)        
        #print(copyListHead.val,copyListHead.next,copyListHead.random)
        return cloneHead
            
            