# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = []
        def recur(root,path):
            if root == None:
                return
            
            recur(root.left,path+str(root.val))
            recur(root.right,path+str(root.val))
            
            if root.left == None and root.right == None:
                res.append(path+str(root.val))
        
            return
        
        recur(root,"")
        res = [int(x) for x in res]
        res = sum(res)
        
        return res