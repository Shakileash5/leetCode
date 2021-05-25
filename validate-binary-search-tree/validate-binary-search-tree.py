# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self,root,temp):
        if root == None:
            return True
        if self.inorder(root.left,temp) == False:
            return False
        if temp==[] or temp[-1]<root.val:
            temp.append(root.val)
        else:
            return False
        if self.inorder(root.right,temp) == False:
            return False
        return True
    
    def isValidBST(self, root: TreeNode) -> bool:
        
        res = []
        def recur(root):
            
            if root == None:
                return True
            
            v = recur(root.left)
            if v == False:
                return False
            if res==[] or res[-1] < root.val:
                res.append(root.val)
            else:
                return False
            u = recur(root.right)
            if u == False:
                return False
        
        #result = recur(root)
        #if result == None:
        #    return True
        #else:
        #    return False
        return self.inorder(root,[])    
        