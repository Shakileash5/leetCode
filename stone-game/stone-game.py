class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        size = len(piles)
        dp = [[None,None] for i in range(size+2)]
        
        def gamePlay(nums,turn):
            if len(nums) == 0:
                return 0
            #print(turn,nums)
            if dp[len(nums)][turn] == None or True:
                if turn == 0:
                    takeFront = gamePlay(nums[1:],1) + nums[0]
                    takeEnd = gamePlay(nums[:-1],1) + nums[-1]
                    dp[len(nums)][turn] = max(takeFront,takeEnd)
                    return dp[len(nums)][turn]
                else:
                    takeFront = gamePlay(nums[1:],0)
                    takeEnd = gamePlay(nums[:-1],0)
                    dp[len(nums)][turn] = min(takeFront,takeEnd)
                    return dp[len(nums)][turn]
            else:
                return dp[len(nums)][turn]
        return True
        score = gamePlay(piles,0)
        print(score)
        return score>(sum(piles)//2)