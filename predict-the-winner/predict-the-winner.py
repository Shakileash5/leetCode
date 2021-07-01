class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        size = len(nums)
        
        memo = {}
        
        def simulateGame(arr,turn):
            if not arr:
                return 0
            if (arr,turn) not in memo:
                if turn == 1:
                    resTake = simulateGame(arr[1:],0) + arr[0]
                    resTakeEnd = simulateGame(arr[:-1],0) + arr[-1]
                    memo[(arr,turn)] = max(resTake,resTakeEnd)
                    return memo[(arr,turn)]
                else:
                    resTake = simulateGame(arr[1:],1)
                    resTakeEnd = simulateGame(arr[:-1],1)
                    memo[(arr,turn)] = min(resTake,resTakeEnd)
                    return memo[(arr,turn)]
            else:
                return memo[(arr,turn)]
        
        return simulateGame(tuple(nums),1)>= sum(nums)/2 