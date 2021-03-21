# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        dp=[[None for _ in range(n+1)] for _ in range(n+1)]
        def solve(start,end):
            print(f"start={start},end={end}")
            
            if start>end:
                return [None]
            if dp[start][end] is not None:
                return dp[start][end]
            if start==end:
                dp[start][end]=[TreeNode(start)]
                return dp[start][end]

            ans=[]
            for i in range(start,end+1):
                lefts=solve(start,i-1)
                rights=solve(i+1,end)
                for left in lefts:
                    for right in rights:
                        root=TreeNode(i,left=left,right=right)
                        ans.append(root)
            dp[start][end]=ans
            return ans
                 
        solve(1,n)
        return dp[1][n]