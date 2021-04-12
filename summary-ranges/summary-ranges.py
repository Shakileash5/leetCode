class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        size = len(nums)
        if size == 0:
            return []
        rangeList = []
        start = nums[0]
        end = nums[0]
        countIdx = start+1
        
        for i in range(1,size):
            #print(countIdx)
            if countIdx == nums[i]:
                end = nums[i]
                
            else:
                if start == end:
                    rangeList.append(str(start))
                else:
                    rangeList.append(str(str(start)+"->"+str(end)))
                #print(start,end,nums[i])
                start = nums[i]
                end = nums[i]
                countIdx = nums[i]
                
            countIdx+=1
        
        if start == end:
            rangeList.append(str(start))
        else:
            rangeList.append(str(str(start)+"->"+str(end)))
        
        return (rangeList)
                    