class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        bothOdd = 0
        lowOdd = 0
        highOdd = 0
        bothEven = 0
        count = 0
        
        if low%2 == 0 and high%2 == 0:
            bothOdd = 1
        else:
            if low%2 != 0:
                low += 1
                count += 1
            if high%2 != 0:
                high += 1
        
        count += (high - low)//2
        return count
            
            