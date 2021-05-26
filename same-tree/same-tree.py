# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameSolTwo(self,rootP,rootQ):
        if rootP == None and rootQ == None:
            print("hereBoth",rootP,rootQ)
            return True
        elif rootP == None and rootQ or rootQ == None and rootP:
            print("here",rootP,rootQ)
            return False
        if rootP.val != rootQ.val:
            return False
        res1 = self.isSameSolTwo(rootP.left,rootQ.left)
        res2 = self.isSameSolTwo(rootP.right,rootQ.right)
        #print(rootP.val,rootQ.val)
        if res1 == res2 and res1 == True:
            return True
        else:
            return False
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        """ def isSame(root1,root2):
            if root1==None and root2==None:
                return True
            elif root1!=None and root2!=None:
                if root1.val == root2.val:
                    res1 = isSame(root1.left,root2.left)
                    res2 = isSame(root1.right,root2.right)
                    
                    if res1==res2 and res1==True:
                        return True
                    else:
                        return False
            return False"""
        
        #return isSame(p,q)
        return self.isSameSolTwo(p,q)