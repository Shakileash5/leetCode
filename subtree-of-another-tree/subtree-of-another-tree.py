# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        def isSubRoot(root1,root2):
            if root1 == None and root2 == None:
                return True
            if (root1==None and root2 ) or (root1 and root2==None ):
                return False
            
            if isSubRoot(root1.left,root2.left)==False:
                return False
            
            if root1.val != root2.val:
                return False
            
            if isSubRoot(root1.right,root2.right)==False:
                return False
            
            return True
        
        def inorder(root,subRoot):
            if root == None:
                return 
            
            if inorder(root.left,subRoot):
                return True
            
            if root.val == subRoot.val:
                if isSubRoot(root,subRoot):
                    return True
            if inorder(root.right,subRoot):
                return True
            return False
        
        return inorder(root,subRoot)
            