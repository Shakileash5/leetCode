# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root == None:
            return None
        
        #if root.left and root.right:
        leftSubtree = root.left
        rightSubtree = root.right
        
        def recur(root1,root2,parent):
            if root1 == None and root2 == None:
                return
            
            #root1.val,root2.val = root2.val,root1.val
            parent.left = root2
            parent.right = root1
            if root1:
                recur(root1.left,root1.right,root1)
            if root2:
                recur(root2.left,root2.right,root2)
            #print(root1.val,root2.val)
            
            return
        
        recur(leftSubtree,rightSubtree,root)
        #print(leftSubtree)
        return root
        