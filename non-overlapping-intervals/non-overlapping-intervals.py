class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        print(intervals)
        size = len(intervals)
        res = 0
        start = intervals[0]
        for i in range(1,size):
            if intervals[i][0]<start[1]:
                if i+1<size:
                    if intervals[i][1]>intervals[i+1][0]:
                        res += 1
                        print("middle")
                    else:
                        res+=1
                        start = intervals[i]
                else:
                    res+=1
            else:
                start = intervals[i]
            print(res)
        
        
        return res