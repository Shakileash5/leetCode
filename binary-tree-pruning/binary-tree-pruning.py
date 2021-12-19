# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(root):
            if root == None:
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            
            if root.left == None and root.right == None and root.val == 0:
                return None
            return root
        
        def dfs2(root):
            if root == None:
                return None,False
            
            root.left,flag1 = dfs2(root.left)
            root.right,flag2 = dfs2(root.right)
            if flag1 == False:
                root.left = None
            if flag2 == False:
                root.right = None
            if flag1 == False and flag2 == False and root.val == 0:
                return None,False
            return root,True
            
        root,flag = dfs2(root)
        return root