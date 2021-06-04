# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self,root,k):
        if root == None:
            return False
        left = self.recur(root.left,k)
        if left  == True:
            return True
        if self.count == k:
            self.val = root.val
            return True
        self.count+=1
        right = self.recur(root.right,k)
        if right == True:
            return True
        return False
        
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def inorder(root):
            if root==None:
                return 0
            if inorder(root.left) == 1:
                return 1
            if inorder.count == k:
                inorder.val = root.val
                return 1
            inorder.count+=1
            if inorder(root.right) == 1:
                return 1
        
        #inorder.count = 1
        #inorder.val = -1
        #inorder(root)
        #
        #return inorder.val
        self.count = 1
        self.val = 0
        self.recur(root,k)
        return self.val
        