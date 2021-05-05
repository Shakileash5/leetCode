class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxHeight = 0
        size = len(gain)
        tempGain = 0
        for i in range(0,size):
            tempGain = tempGain+gain[i]
            maxHeight = max(maxHeight,tempGain)
        
        return maxHeight