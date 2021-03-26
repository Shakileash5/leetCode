# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def structTree(postOrder,inOrder,left,right):
            
            if left>right:
                return None
            
            node = TreeNode(postOrder[postOrderIdx[0]])
            postOrderIdx[0]-=1
            
            if left==right:
                return node
            #print(node)
            idx = search(inOrder,left,right,node.val)
            
            
            node.right = structTree(postOrder,inOrder,idx+1,right)
            node.left = structTree(postOrder,inOrder,left,idx-1)
            
            return node
        
        def search(inOrder,left,right,target):
            for i in range(left,right+1):
                if inOrder[i] == target:
                    return i
            return None
        
        size = len(inorder)
        postOrderIdx = [size-1]
        tree = structTree(postorder,inorder,0,size-1)
        return tree
        