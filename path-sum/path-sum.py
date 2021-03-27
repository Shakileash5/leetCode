# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def recurInorder(root,pathSum):
            
            if root == None:
                return None
            
            
            
            if recurInorder(root.left,pathSum+root.val) == True:
                return True
            
            if recurInorder(root.right,pathSum+root.val) == True:
                return True
            
            #print(root.val,pathSum+root.val)
            if root.left==None and root.right==None and pathSum+root.val == targetSum:
                return True
            return False
        
        return recurInorder(root,0)
            
            
            
        