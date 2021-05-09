# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        def recur(root1,root2):
            
            if root1==None and root2==None:
                return None
            node = TreeNode()
            if root1 and root2:
                root1.val = root1.val+root2.val
                
                
            if root1 ==None:
                return root2
            
            if root2 == None:
                return root1
             
            root1.left = recur(root1.left,root2.left)
            root1.right = recur(root1.right,root2.right)
            
            return root1
        
        return recur(root1,root2)