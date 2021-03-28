# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def recur(root,parent):
            if root == None :
                return
            
            flag = False
            
            if root.left or root.right:
                parent = root
                flag = True
            
            recur(root.left,parent)
            recur(root.right,parent)
            print("parent",parent,root.val)
            if root.left :
                temp = root.left
                while(temp.right):
                    temp = temp.right
                print("temp",temp)
                temp.right = parent.right
                root.right = root.left
                root.left = None
                print("parent",parent,"\n")
            
            return
        
        recur(root,None)