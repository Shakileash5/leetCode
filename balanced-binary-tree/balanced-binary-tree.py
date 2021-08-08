# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(root):
            if root == None:
                return 0
            
            return max(getHeight(root.left),getHeight(root.right))+1
        
        #print(getHeight(root))
        
        def isBalancedHelper(root):
            if root == None:
                return True
            
            lHeight = getHeight(root.left)
            rHeight = getHeight(root.right)
            if abs(lHeight-rHeight)>1:
                return False
            if isBalancedHelper(root.left) == False:
                return False
            if isBalancedHelper(root.right) == False:
                return False
            return True
        
        return isBalancedHelper(root)
            