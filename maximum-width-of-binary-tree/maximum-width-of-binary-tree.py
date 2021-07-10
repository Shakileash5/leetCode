# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        maxWidth = 1
        queue = [(root,0)]
        queueUtil = []
        
        while(queue):
            node = queue.pop(0)
            if node[0].left:
                queueUtil.append((node[0].left,node[1]*2))
            if node[0].right:
                queueUtil.append((node[0].right,node[1]*2+1))
            
            if queue == []:
                if queueUtil:
                    #print(queueUtil)
                    #print(queueUtil[-1][1] - queueUtil[0][1] + 1)
                    width = queueUtil[-1][1] - queueUtil[0][1] + 1
                    maxWidth = max(maxWidth,width)
                    queue = queueUtil[:]
                queueUtil = []
        
        return maxWidth