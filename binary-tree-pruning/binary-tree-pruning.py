# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def recur(root):
            if root == None:
                return None
            
            root.left = recur(root.left)
            root.right = recur(root.right)
            
            if root.left == None and root.right == None and root.val == 0:
                return None
            return root
        
        return recur(root)
            
            