# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        resQueqe = []
        resQueqe.append(root)
        resQueqeAlter = []
        count = 0
        zigZag = []
        levelOrder =[]
        
        while(len(resQueqe)>0):
            res = resQueqe.pop(0)
            if len(levelOrder)<count+1:
                print(count)
                if (count)%2==0 and count !=0:
                    levelOrder[-1] = levelOrder[-1][::-1]
                    print(levelOrder,count)
                levelOrder.append([res.val])
            else:
                levelOrder[count].append(res.val)
            #print(res.val)
            if res.left!=None:
                resQueqeAlter.append(res.left)
            if res.right!=None:
                resQueqeAlter.append(res.right)
            if len(resQueqe)==0:
                #print(resQueqeAlter)
                resQueqe = resQueqeAlter[:]
                resQueqeAlter = []
                count+=1
        print(levelOrder,count)
        if count%2==0:
            levelOrder[-1] = levelOrder[-1][::-1]
        return levelOrder
            