# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def structTreeTwo(self,preorder,inorder,left,right):
        if left>right:
            return None
        node = TreeNode(preorder[self.preorderIdx[0]])
        self.preorderIdx[0]+=1
        if left == right:
            return node
        rootIdx = self.search(inorder,left,right,node.val)
        node.left = self.structTreeTwo(preorder,inorder,left,rootIdx-1)
        node.right = self.structTreeTwo(preorder,inorder,rootIdx+1,right)
        return node
    def search(self,inorder,left,right,target):
        for i in range(left,right+1):
            if inorder[i] == target:
                return i
        return -1
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def structTree(preOrder,inOrder,left,right):
            
            if left>right:
                return None
            
            treeNode = TreeNode(preOrder[preOrderIdx[0]])
            preOrderIdx[0]+=1
            
            if left == right:
                return treeNode
            
            rootIdx = search(inOrder,left,right,treeNode.val)
            
            treeNode.left = structTree(preOrder,inOrder,left,rootIdx-1)
            treeNode.right = structTree(preOrder,inOrder,rootIdx+1,right)
            
            return treeNode
        
        def search(inOrder,left,right,target):
            for i in range(left,right+1):
                if inOrder[i] == target:
                    return i
            return None
        preOrderIdx = [0]
        self.preorderIdx = [0]
        #tree = structTree(preorder,inorder,0,len(inorder)-1)
        #print(tree)
        #return tree
        return self.structTreeTwo(preorder,inorder,0,len(preorder)-1)
        