# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def getDiameter(root):
            if root == None:
                return 0
            
            left = getDiameter(root.left)
            right = getDiameter(root.right)
            diameter = left+right
            getDiameter.diameter = max(getDiameter.diameter,diameter)
            return max(left,right) + 1
        getDiameter.diameter  = 0
        getDiameter(root)
        return getDiameter.diameter