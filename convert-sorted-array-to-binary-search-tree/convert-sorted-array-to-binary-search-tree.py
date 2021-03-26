# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        
        def buildTree(arr,left,right):
            if left>right:
                return None
            #size = len(arr[left:right+1])
            mid = (left+right)//2
            node = TreeNode(arr[mid])
            
            if left==right:
                return node
            
            node.left = buildTree(arr,left,mid-1)
            node.right = buildTree(arr,mid+1,right)
            
            return node
        
        tree = buildTree(nums,0,len(nums)-1)

        return tree
        