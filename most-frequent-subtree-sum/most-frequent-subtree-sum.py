# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        hashMap = {}
        
        def dfs(root,sum_):
            if root == None:
                return 0
            
            lSubtree = dfs(root.left,sum_+root.val)
            rSubtree = dfs(root.right,sum_+root.val)
            #print(root.val,lSubtree,rSubtree,"w",root.val+lSubtree+rSubtree)
            val = root.val+lSubtree+rSubtree
            if val not in hashMap:
                hashMap[val] = 1
            else:
                hashMap[val] += 1
            return val
        
        #print(dfs(root,0))
        dfs(root,0)
        #print(hashMap)
        res = []
        freq = None
        for key in hashMap:
            if freq == None:
                freq = hashMap[key]
                res.append(key)
            elif hashMap[key]>freq:
                freq = hashMap[key]
                res = [key]
            elif hashMap[key]==freq:
                res.append(key)
        return res
        