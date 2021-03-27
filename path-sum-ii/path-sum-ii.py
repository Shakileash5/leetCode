# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        res = []
        
        def recurInorder(root,pathSum,pathSumList):
            
            if root == None:
                return None
    
            recurInorder(root.left,pathSum+root.val,pathSumList+[root.val])
            
            recurInorder(root.right,pathSum+root.val,pathSumList+[root.val])            
            #print(root.val,pathSum+root.val)
            if root.left==None and root.right==None and pathSum+root.val == targetSum:
                pathSumList.append(root.val)
                #print(pathSumList)
                res.append(pathSumList)
                
            
            return 
        
        recurInorder(root,0,[])
        return res