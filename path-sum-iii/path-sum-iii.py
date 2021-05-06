# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        
        count = [0]
        resPaths = []
        def recur(root,path):
            
            #print(path
            if root == None:
                return
            """if path!=[]:
                #print(path)
                if sum(path) == targetSum:
                    count[0]+=1
                    #print("yes")
                    resPaths.append(path)
                if sum(path)!=targetSum:
                    dif = sum(path) - targetSum
                    if dif in path:
                        
                        temp = path[:]
                        temp.remove(dif)
                        if temp not in resPaths:
                            count[0]+=1
                            resPaths.append(temp)
                            #print("yes in diff",dif,temp,resPaths)"""
            sumVal = 0
            for i in range(len(path)-1,-1,-1):
                sumVal += path[i]
                if sumVal == targetSum:
                    count[0]+=1
            if root.left:
                recur(root.left,path+[root.left.val])
            if root.right:
                recur(root.right,path+[root.right.val])
            
            return
        if root:
            recur(root,[root.val])
        
        return count[0]            