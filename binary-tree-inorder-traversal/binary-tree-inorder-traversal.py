# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #print(root)
        res = []
        def inorder(head):
            if head == None:
                return
            inorder(head.left)
            res.append(head.val)
            inorder(head.right)
        
        inorder(root)
        return(res)
        