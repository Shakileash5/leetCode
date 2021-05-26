# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root,res):
            if root == None:
                return
            inorder(root.left,res)
            res.append(root.val) 
            inorder(root.right,res)
            return
        def inorderRestore(root,res):
            if root == None:
                return
            inorderRestore(root.left,res)
            #print(root.val,res)
            if root.val != res[0]:
                #print("inside")
                root.val = res[0]
            res.pop(0)
            inorderRestore(root.right,res)
            return
        res = []
        inorder(root,res)
        print(res)
        res.sort()
        print(res)
        inorderRestore(root,res)
        
        return