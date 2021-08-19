# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        queue = [root1]
        queue2 = [root2]
        queueUtils = []
        queueUtils2 = []
        
        if root1 is None and root2 is None:
            return True
        elif root1 is None and root2 is not None or root1 is not None and root2 is None:
            return False
        
        else:
            if root1.val != root2.val:
                return False
            while queue:
                if queue2:
                    temppo = queue2.pop(0)
                else:
                    temppo = None
                temp = queue.pop(0)
                
                if temppo and temp:
                    if (temp.left and temppo.right and temp.left.val == temppo.right.val) or  (temp.right and temppo.left and temp.right.val == temppo.left.val):

                        temp.left, temp.right = temp.right, temp.left
                        #if self.isSameTree(root1, root2) == True:
                        #    return True
                
                if temp.left is not None:
                    queueUtils.append(temp.left)
                if temp.right is not None:
                    queueUtils.append(temp.right)
                    
                if temppo:
                    if temppo.left is not None:
                        queueUtils2.append(temppo.left)
                    if temppo.right is not None:
                        queueUtils2.append(temppo.right)
                
                
                if len(queue) == 0:
                    if queueUtils:
                        queue = queueUtils[:]
                        queueUtils = []
                if len(queue2) == 0:
                    if queueUtils2:
                        queue2 = queueUtils2[:]
                        queueUtils2 = []
                        
            if self.isSameTree(root1, root2) == True:
                return True
                
            return False
        
        
        
    def isSameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2 is not None or root1 is not None and root2 is None:
            return False
        if root1.val != root2.val:
            return False
        if self.isSameTree(root1.left, root2.left) == True and self.isSameTree(root1.right, root2.right) == True:
            return True
        else:
            return False