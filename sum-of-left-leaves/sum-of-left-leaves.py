# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        sum_ = [0]
        def recur(root,parent):
            if root == None:
                return
            if parent!=None and parent.left and root == parent.left:
                if root.left == None and root.right == None:
                    sum_[0] += root.val
            recur(root.left,root)
            recur(root.right,root)
            return
        
        recur(root,None)
        return sum_[0]