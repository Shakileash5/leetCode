"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def cloneListSol(self,head):
        if head == None:
            return None
        
        hashMap = {}
        size = 0
        cloneList = []
        tempHead = head
        count = 0
        
        while head:
            head.checkIdx = count
            count+=1
            node = Node(head.val)
            cloneList.append(node)
            head = head.next
        
        head = tempHead
        size = count 
        #print(count,size)
        count = 0
        #print(len(cloneList))
        while head:
            if count == size-1:
                cloneList[count].next = None
            else:
                #print(count)
                cloneList[count].next = cloneList[count+1]
            
            if head.random:
                cloneList[count].random = cloneList[head.random.checkIdx]
            else:
                cloneList[count].random = None
            
            count+=1
            head = head.next
        
        
        return cloneList[0]
    
    
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        def copyRandomSol():
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
            return cloneHead




            #print(copyList)        
            #print(copyListHead.val,copyListHead.next,copyListHead.random)
        return self.cloneListSol(head)
        
            
            