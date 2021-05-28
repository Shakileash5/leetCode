# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDeptTwo(self,root):
        if root == None:
            return 0
        
        res = self.minDeptTwo(root.left)
        res2 = self.minDeptTwo(root.right)
        
        if res == 0 and res2 != 0:
            return res2 +1
        elif res != 0 and res2 == 0:
            return res + 1
        else:
            return min(res,res2)+1
    
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
        
        #recur(root,1)
        #return minHeight[0]
        return self.minDeptTwo(root)