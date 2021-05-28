# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedTwo(self,root):
        def height(root):
            if root == None:
                return 0
            
            return max(height(root.left),height(root.right)) + 1
        
        def recur(root):
            if root == None:
                return True
            
            heightL = height(root.left)
            heightR = height(root.right)
            
            if abs(heightL-heightR)>1:
                return False
            
            if recur(root.left) == False:
                return False
            if recur(root.right) == False:
                return False
            
            return True
            
        #print()
        return recur(root)
        
        
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root == None:
            return True
        
        def height(root,hh,high):
            if root == None:
                return None
            if high[0]<hh:
                high[0] = hh
            
            height(root.left,hh+1,high)
            height(root.right,hh+1,high)
            
            return high[0]
        
        def recur(root,leftHigh,rightHigh):
            
            if root == None:
                return
            
            high = [0]
            lh = 0
            if root.left:
                lh = height(root.left,1,high)
            high = [0]
            rh = 0
            if root.right:
                rh = height(root.right,1,high)
            #print(root.val,lh,rh,leftHigh,rightHigh)
            if abs(lh-rh)>1:
                return False
            if recur(root.left,leftHigh+1,rightHigh) == False:
                return False
            if recur(root.right,leftHigh,rightHigh+1) == False:
                return False
            
            return True
        
        #return recur(root,1,1)
        return self.isBalancedTwo(root)