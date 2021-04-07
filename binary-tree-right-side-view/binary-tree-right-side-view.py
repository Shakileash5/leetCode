# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if root == None:
            return []
        
        res = [root.val]
        Queue = []
        Queue.append(root)
        QueueUtil = []
        
        while(Queue):
            node = Queue.pop()
            #print("node",node)
            if node.left:
                QueueUtil.append(node.left)
            if node.right:
                QueueUtil.append(node.right)
            
            if Queue == []:
                #print(QueueUtil)
                Queue = QueueUtil[::-1]
                if len(QueueUtil)!=0:
                    res.append(QueueUtil[-1].val)
                QueueUtil = []
        
        return res