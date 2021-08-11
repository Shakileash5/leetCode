# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root == None:
                return 0
            
            left = dfs(root.left)+1
            if left == float('inf'):
                return float('inf')
            
            right = dfs(root.right)+1
            
            if abs(left-right)>1:
                return float('inf')
            else:
                return max(left,right)
        
        return dfs(root) != float('inf')