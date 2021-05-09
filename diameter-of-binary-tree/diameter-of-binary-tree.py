# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.max_ = 0
        def diameter(rootNode):
            if rootNode == None:
                return 0 
            lDiameter = diameter(rootNode.left)
            rDiameter = diameter(rootNode.right)
            
            if lDiameter+rDiameter>self.max_:
                self.max_ = lDiameter+rDiameter
            return 1+max(lDiameter,rDiameter)
        diameter(root)
        return self.max_
        
        
                
            