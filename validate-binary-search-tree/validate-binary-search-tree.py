# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        
        def inorder(root):
            if root == None:
                return True
            
            if inorder(root.left) == False:
                return False
            if res == [] or res[-1]<root.val:
                res.append(root.val)
            else:
                return False
            if inorder(root.right) == False:
                return False
            return True
        
        return inorder(root)
            