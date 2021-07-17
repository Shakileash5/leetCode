# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        
        def recur(root):
            if root == None:
                return root
            
            if root.val<low:
                root = recur(root.right)
                return root
            if root.val>high:
                root = recur(root.left)
                return root
            
            root.left = recur(root.left)
            root.right = recur(root.right)
            return root
        
        return recur(root)
            
            
            
            