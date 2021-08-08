# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorderIdx = [0]
        def buildTreeHelper(preorderIdx,left,right):
            if left>right:
                return None
            
            node = TreeNode(preorder[preorderIdx[0]])
            idx = search(preorder[preorderIdx[0]],left,right)
            preorderIdx[0] += 1
            if left == right:
                return node
            
            node.left = buildTreeHelper(preorderIdx,left,idx-1)
            node.right = buildTreeHelper(preorderIdx,idx+1,right)
            return node
        
        def search(target,left,right):
            for i in range(left,right+1):
                if inorder[i] == target:
                    return i
            return -1
        
        return buildTreeHelper(preorderIdx,0,len(preorder)-1)
            