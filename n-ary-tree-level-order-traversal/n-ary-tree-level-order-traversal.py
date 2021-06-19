"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        queue = []
        queueUtil = []
        if root == None:
            return []
        queue.append(root)
        res = [[root.val]]
        resUtil = []
        while queue:
            node = queue.pop(0)
            #print(node.val)    
            for children in node.children:
                queueUtil.append(children)
                resUtil.append(children.val)
            if queue == []:
                if queueUtil != []:
                    queue = queueUtil[:]
                    res.append(resUtil[:])
                queueUtil = []
                resUtil = []
        
        return res