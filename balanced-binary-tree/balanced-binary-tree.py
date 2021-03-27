# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root == None:
            return True
        high = [0]
        def height(root,hh,high):
            if root == None:
                return None
            if high[0]<hh:
                high[0] = hh
            
            height(root.left,hh+1,high)
            height(root.right,hh+1,high)
            
            return high[0]
        
        height(root,1,high)
        print(high[0])    
        
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
            print(root.val,lh,rh)
            if abs(lh-rh)>1:
                return False
            if recur(root.left,leftHigh+1,rightHigh) == False:
                return False
            
            if recur(root.right,leftHigh,rightHigh+1) == False:
                return False
            
            
            return True
        
        return (recur(root,1,1))