# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        
        def dfs(root):
            if root == None:
                return None
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            #print(root.val,root.left,root.right,res)
            if root.val in to_delete:
                #print("fs")
                if root.left == None and root.right:
                    res.append(root.right)
                    #print(res)
                    #return None
                if root.right == None and root.left:
                    res.append(root.left)
                    #print(res)
                    #return None
                elif root.left and root.right:
                    res.append(root.right)
                    res.append(root.left)
                    #return None
                #print(res,"s")
                return None
            return root
        
        res.append(dfs(root))
        if None in res:
            res.remove(None)
        return res
                