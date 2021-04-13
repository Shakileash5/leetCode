# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def isChildPresent(rootNode,child):
            if rootNode == None:
                return 
            if rootNode == child:
                return True
            
            if isChildPresent(rootNode.left,child) == True:
                return True
            if isChildPresent(rootNode.right,child) == True:
                return True
        
        def LCA(rootNode):
            if rootNode == None:
                return 
            if LCA(rootNode.left) == True:
                return True      
            if LCA(rootNode.right) == True:
                return True
            #print(rootNode.val,"val")
            if isChildPresent(rootNode,p) and isChildPresent(rootNode,q):
                #print(rootNode.val)
                LCA.node = rootNode
                return True
        
        LCA.node = None
        LCA(root)
        return LCA.node