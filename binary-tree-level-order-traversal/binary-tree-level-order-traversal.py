# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        res = []
        rootTemp = root
        maxDepth = [-1]
        
        def recurDepth(root,maxLevel):
            if root==None:
                return 
            recurDepth(root.left,maxLevel+1)
            if maxDepth[0]<maxLevel:
                maxDepth[0] = maxLevel
            recurDepth(root.right,maxLevel+1)
            
            return
        
        recurDepth(rootTemp,0)
        res = [None]*(maxDepth[0]+1)
        
        def recur(root,level):
            if root==None:
                return
            
            recur(root.left,level+1)
            if res[level] == None:
                res[level] = [root.val]
            else:
                res[level].append(root.val)
            #print(level,root.val,res)   
            recur(root.right,level+1)
            
            return
        
        recur(root,0)
        #print(res)
        return res