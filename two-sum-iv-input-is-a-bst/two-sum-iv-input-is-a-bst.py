# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        tempRoot = [root]
        def searchBst(root,target,node):
            if root == None:
                return False
            
            if target<root.val:
                if searchBst(root.left,target,node):
                    return True
            
            if target>root.val:
                if searchBst(root.right,target,node):
                    return True
            
            if target == root.val and root != node:
                return True
            
            return False
        
        def twoSum(root):
            if root == None:
                return False
            
            if twoSum(root.left):
                return True
            
            target = k - root.val
            if target<root.val:
                if searchBst(root.left,target,root):
                    return True
            else:
                if searchBst(tempRoot[0],target,root):
                    return True
            if twoSum(root.right):
                return True
        
            return False
        
        return twoSum(root)

                
                
            
            
            
            