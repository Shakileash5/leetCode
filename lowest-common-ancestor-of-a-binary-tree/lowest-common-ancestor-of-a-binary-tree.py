# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def LCA(self,root,p,q):
        def searchNode(root,node):
            if root == None:
                return False
            if root == node:
                return True
            if searchNode(root.left,node):
                return True
            if searchNode(root.right,node):
                return True
            
            return False
        
        def getLCA(root,nodeA,nodeB):
            if root == None:
                return False
            
            left = getLCA(root.left,nodeA,nodeB)
            if left != False:
                return left
            
            right = getLCA(root.right,nodeA,nodeB)
            if right != False:
                return right
            
            isNodeA = searchNode(root,nodeA)
            isNodeB = searchNode(root,nodeB)
            if isNodeA and isNodeB:
                return root
            return False
        
        return getLCA(root,p,q)
    
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
        
        def LCAOptimised(root,n1,n2):
            if root == None:
                return None
            
            if root.val == n1.val or root.val == n2.val:
                return root
            
            leftSubtree = LCAOptimised(root.left,n1,n2)
            rightSubtree = LCAOptimised(root.right,n1,n2)
            
            if leftSubtree and rightSubtree:
                return root
            
            if leftSubtree != None:
                return leftSubtree
            return rightSubtree
            
        
        #LCA.node = None
        #LCA(root)
        #return LCAOptimised(root,p,q)
        
        return self.LCA(root,p,q)