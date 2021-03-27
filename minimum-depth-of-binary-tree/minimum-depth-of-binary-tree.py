# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        minHeight = [10000]
        
        def recur(root,height):
            if root == None:
                return
            
            if root.left==None and root.right==None:
                if minHeight[0] > height:
                    minHeight[0] = height
            
            recur(root.left,height+1)
            recur(root.right,height+1)
            
            return
        
        recur(root,1)
        return minHeight[0]
        