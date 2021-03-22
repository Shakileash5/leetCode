# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
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
        
        return isSymmentry(root,root)
        