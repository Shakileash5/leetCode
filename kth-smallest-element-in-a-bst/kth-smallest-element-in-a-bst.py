# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = [0]
        def inorder(root):
            if root == None:
                return False
            if inorder(root.left):
                return True
            count[0] += 1
            if count[0] == k:
                count[0] = root.val
                return True
            if inorder(root.right):
                return True
            
            return False
        
        inorder(root)
        return count[0]