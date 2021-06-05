# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePathsTwo(self,root):
        path = []
        
        def recur(root,tempPath):
            if root == None:
                return
            recur(root.left,tempPath+str(root.val)+"->")
            if root.left == None and root.right == None:
                path.append(tempPath+str(root.val))
            recur(root.right,tempPath+str(root.val)+"->")
            
            return
        
        recur(root,"")
        return path
            
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        path = []
        
        def isLeaf(node):
            if node == None:
                return False
            if node.left == None and node.right == None:
                return True    
            return False
        
        if isLeaf(root):
            return [str(root.val)]
        
        
        def inorder(node,tempPath):
            if node == None:
                return
            
            inorder(node.left,tempPath+"->"+str(node.val))
            if isLeaf(node) == True:
                path.append(tempPath[2:]+"->"+str(node.val))
            inorder(node.right,tempPath+"->"+str(node.val))
            
            return
        
        #inorder(root,"")
        #return path
        return self.binaryTreePathsTwo(root)