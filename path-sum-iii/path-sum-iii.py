# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSumTwo(self,root,target,temp):
        if root == None:
            return 
        #print(sum_,root.val)
        #if sum_+root.val>=target:
        sumCheck = 0
        temp.append(root.val)
        for i in range(len(temp)-1,-1,-1):
            sumCheck += temp[i]
            if sumCheck == target:
                self.count +=1
        temp.pop()
        
        self.pathSumTwo(root.left,target,temp+[root.val])
        self.pathSumTwo(root.right,target,temp+[root.val])
    
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        
        count = [0]
        
        def recur(root,path,pathSum):
            
            #print(path
            if root == None:
                return
            
            sumVal = 0
            for i in range(len(path)-1,-1,-1):
                sumVal += path[i]
                if sumVal == targetSum:
                    count[0]+=1
            if root.left:
                recur(root.left,path+[root.left.val],pathSum)
            if root.right:
                recur(root.right,path+[root.right.val],pathSum)
            
            return
        #if root:
        #    recur(root,[root.val],0)
        #return count[0] 
        print(root)
        self.count = 0
        self.pathSumTwo(root,targetSum,[])
        return self.count