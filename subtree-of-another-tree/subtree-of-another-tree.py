# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        def isSubTreeUtil(root1,root2):
            if root1 == None or root2 == None:
                if root1 == None and root2 == None:
                    return True
                return False
            
            if isSubTreeUtil(root1.left,root2.left) == False:
                return False
            
            if root1.val != root2.val:
                return False
            
            if isSubTreeUtil(root1.right,root2.right) == False:
                return False
            
            return True
        
        def checkSubroot(root,subRoot):
            if root == None:
                return False
            
            if checkSubroot(root.left,subRoot):
                return True
            
            if isSubTreeUtil(root,subRoot):
                return True
            
            if checkSubroot(root.right,subRoot):
                return True
            
            return False
        
        return checkSubroot(root,subRoot)
            