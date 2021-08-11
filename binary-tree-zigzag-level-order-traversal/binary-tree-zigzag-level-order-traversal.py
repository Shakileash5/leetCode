# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            This function returns the zigzag order of the tree
        '''
        
        if root == None:
            return []
        
        queue = [] # queue to perform bfs
        queueUtil = [] # util queue to keep track of childrens of the present level
        
        res = [] 
        resUtil = []
        count = 0 # to keep Track of the odd and even level 
        
        queue.append(root)
        res.append([root.val])
        
        while(queue):
            while(queue):
                # store every children from current level into queueUtil
                node = queue.pop(0)
                if node.left:
                    queueUtil.append(node.left)
                    resUtil.append(node.left.val)
                if node.right:
                    queueUtil.append(node.right)
                    resUtil.append(node.right.val)
            
            if queue == [] and queueUtil != []:
                queue = queueUtil[:]
                if count %2 == 0:
                    resUtil = resUtil[::-1]
                res.append(resUtil[:])
                resUtil = []
                queueUtil = []
            count += 1
                
        return res
                