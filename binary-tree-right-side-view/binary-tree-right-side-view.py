# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        queue = [root]
        res = [root.val]
        queueUtil = []
        while queue:
            while queue:
                node = queue.pop(0)
                if node.left:
                    queueUtil.append(node.left)
                if node.right:
                    queueUtil.append(node.right)
            if queueUtil:
                res.append(queueUtil[-1].val)
            queue = queueUtil[:]
            queueUtil = []
        
        return res
                    