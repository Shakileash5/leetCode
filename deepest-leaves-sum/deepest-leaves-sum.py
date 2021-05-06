# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        res = 0
        queue = []
        queueUtil = []
        val = 0
        queue.append(root)
        
        while(queue):
            child = queue.pop(0)
            
            if child.left:
                queueUtil.append(child.left)
                val+=child.left.val
            if child.right:
                queueUtil.append(child.right)
                val+=child.right.val
            
            if len(queue)==0:
                queue = queueUtil[:]
                queueUtil = []
                
                if len(queue)!=0:
                    res = val
                val = 0
                #print(queue)
        return res