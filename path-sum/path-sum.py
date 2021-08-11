# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root,pathSum):
            # This function determines wheather a root to leaf path sum is equal to the target
            if root == None:
                return False
            
            if dfs(root.left,pathSum+root.val):
                return True
            
            if root.left == None and root.right == None and pathSum+root.val == targetSum:
                return True
            
            if dfs(root.right,pathSum+root.val):
                return True
            
            return False
        
        return dfs(root,0)