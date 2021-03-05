# https://leetcode.com/problems/merge-intervals/
# Problem Description

# Solution
class Solution:    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        size = len(intervals)
        res = []
        intervals = sorted(intervals)
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
                    res.append(intervals[i])
        print(res)
        return res        