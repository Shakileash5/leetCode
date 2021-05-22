class Solution:    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        size = len(intervals)
        res = []
        
        """intervals = sorted(intervals)
        for i in range(size):
            
            if len(res) == 0:
                res.append(intervals[i])
            else:
                temp = res[-1]
                if temp[1]>=intervals[i][0] and temp[0]<=intervals[i][0]:
                    if temp[1]<=intervals[i][1]:
                        temp[1] = intervals[i][1]
                        res.pop()
                        res.append(temp)
                else:
                    res.append(intervals[i])"""
        
        intervals.sort()
        #print(intervals)
        i = 1
        while(i<size):
            #print(intervals,i)
            if intervals[i][0]<=intervals[i-1][1]:
                #print("here",i,size,intervals[i][1])
                if intervals[i][1]<intervals[i-1][1]:
                    #print("whole")
                    del intervals[i]
                else:
                    #print("partial")
                    intervals[i-1][1] = intervals[i][1]
                    del intervals[i]
                size-=1
            else:
                i+=1
        
        #print(intervals)
        return intervals        