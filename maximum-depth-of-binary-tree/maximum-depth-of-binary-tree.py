# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurTwo(self,root):
        if root == None:
            return 0
        height = max(self.recurTwo(root.left),self.recurTwo(root.right))+1
        return height
        
    def maxDepth(self, root: TreeNode) -> int:
        maxDepth = [-1]
        
        def recur(root,maxLevel):
            if root==None:
                return 
            recur(root.left,maxLevel+1)
            if maxDepth[0]<maxLevel:
                maxDepth[0] = maxLevel
            recur(root.right,maxLevel+1)
            
            return
        
        #recur(root,0)
        #print(maxDepth[0])
        #return maxDepth[0]+1
        return self.recurTwo(root)