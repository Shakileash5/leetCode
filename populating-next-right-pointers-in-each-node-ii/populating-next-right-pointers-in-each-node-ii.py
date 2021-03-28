"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root==None:
            return None
        
        Queqe = []
        utilLevel = []
        temp = root
        Queqe.append(root)
        last = None
        while(len(Queqe)!=0):
            root = Queqe.pop(0)
            if root.left:
                if last!=None:
                    last.next = root.left
                utilLevel.append(root.left)
                last = root.left
            if root.right:
                if last!=None:
                    last.next = root.right
                utilLevel.append(root.right)
                last = root.right
                root.right.next = None
            
            if Queqe == []:
                Queqe = utilLevel[:]
                utilLevel = []
                last = None
                
        #print(levelOrder)
        return temp