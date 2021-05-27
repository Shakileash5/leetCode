# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        elif root1==None and root2 or root2==None and root1:
            return False
        if root1.val!=root2.val:
            return False
        res1 = self.isMirror(root1.left,root2.right)
        res2 = self.isMirror(root1.right,root2.left)
        if res2==res1 and res2 == True:
            return True
        else:
            return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        leftTree = root.left
        rightTree = root.right
        
        def isSymmentry(leftRoot,rightRoot):
            if leftRoot==None and rightRoot==None:
                return True
            else:
                if leftRoot != None and rightRoot!=None:
                    if leftRoot.val == rightRoot.val:
                        res1 = isSymmentry(leftRoot.left,rightRoot.right)
                        res2 = isSymmentry(leftRoot.right,rightRoot.left)
                        if res1 == True and res2 == True:
                            return True
                        else:
                            return False
            return False
        
        #return isSymmentry(leftTree,rightTree)
        return self.isMirror(leftTree,rightTree)