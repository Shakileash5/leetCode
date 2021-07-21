# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = [0]
        maxNode = float('-inf')
        
        def dfs(root,maxNode):
            if root == None:
                return
            dfs(root.left,max(maxNode,root.val))
            if root.val>=maxNode:
                goodNodes[0] += 1
            dfs(root.right,max(maxNode,root.val))
            return
        
        dfs(root,maxNode)
        return goodNodes[0]