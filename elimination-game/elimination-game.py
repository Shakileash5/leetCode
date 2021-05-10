class Solution:
    def lastRemaining(self, n: int) -> int:
        
        #nums = list(range(1,n+1))
        
        dir = 1
        nums = n
        start = 1
        step = 1
        
        while(nums>1):
            if dir ==1 or(dir == -1 and nums%2 ==1):
                start += step
            
            dir*=-1
            step*=2
            nums=nums//2
            
        return start
            
        