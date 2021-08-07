# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        hashMap = {}
        
        def dfs(root,level,nodeNum):
            if root == None:
                return
            
            dfs(root.left,level+1,nodeNum*2)
            dfs(root.right,level+1,nodeNum*2+1)
            if level not in hashMap:
                hashMap[level] = [nodeNum]
            else:
                hashMap[level].append(nodeNum)
            
            return
        dfs(root,1,0)
        #print(hashMap)
        maxWidth = 0
        for key in hashMap:
            maxWidth = max(maxWidth,hashMap[key][-1] - hashMap[key][0]+1)
        
        return maxWidth
                