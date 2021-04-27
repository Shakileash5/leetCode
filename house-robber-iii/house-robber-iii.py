# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        @cache
        def dfs(root,taken):
            if root == None:
                return 0
            
            if not taken: 
                #print("here",root.val)
                ifTaken = root.val+dfs(root.left,True)+dfs(root.right,True)
                ifNotTaken = dfs(root.left,False) + dfs(root.right,False)
                
                #print(left,right)
                return max(ifTaken,ifNotTaken)
            
            else:
                #print("notTaken",root.val)
                val1 = dfs(root.left,False)
                #print(root.val,"gotaVal1",val1)
                val2 = dfs(root.right,False)
                #print(root.val,"gotaVal2",val2)
                #print(root.val,"now the vals are" ,val1,val2)
                if val1 and val2:
                    return val1+val2
                elif val1:
                    return val1
                elif val2:
                    return val2
                else: 
                    return 0
        
        
        
        rootTaken = dfs(root.left,True) + dfs(root.right,True) + root.val
        rootNotTaken = dfs(root.left,False) + dfs(root.right,False)
        #print(rootTaken,rootNotTaken)
        
        
        return max(rootTaken,rootNotTaken)