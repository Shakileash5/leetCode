# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagSolTwo(self,root):
        if root == None:
            return []
        res = []
        resUtil = []
        queue = []
        queueUtil = []
        count = 1
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            resUtil.append(node.val)
            if node.left:
                queueUtil.append(node.left)
            if node.right:
                queueUtil.append(node.right)
                
            if queue==[]:
                if count%2==0:
                        resUtil = resUtil[::-1]
                res.append(resUtil[:])
                if queueUtil:
                    queue = queueUtil.copy()
                queueUtil = []
                resUtil = []
                count+=1
        return res
        
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def solutionOne():
            if root == None:
                return []
            resQueqe = []
            resQueqe.append(root)
            resQueqeAlter = []
            count = 0
            zigZag = []

            while(len(resQueqe)>0):
                res = resQueqe.pop(0)
                if len(zigZag)<count+1:
                    if (count)%2==0 and count !=0:
                        zigZag[-1] = zigZag[-1][::-1]
                    zigZag.append([res.val])
                else:
                    zigZag[count].append(res.val)
                if res.left!=None:
                    resQueqeAlter.append(res.left)
                if res.right!=None:
                    resQueqeAlter.append(res.right)
                if len(resQueqe)==0:
                    resQueqe = resQueqeAlter[:]
                    resQueqeAlter = []
                    count+=1

            if count%2==0:
                zigZag[-1] = zigZag[-1][::-1]
        #return zigZag
        return self.zigzagSolTwo(root)    