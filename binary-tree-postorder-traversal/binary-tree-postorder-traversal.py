# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def recur(root):
            if root == None:
                return
            
            recur(root.left)
            recur(root.right)
            res.append(root.val)
            
            return
        
        recur(root)
        #print(res)
        return res