# https://leetcode.com/problems/insert-interval/
# Problem Description

# Solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        size = len(intervals)
        res = []
        
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
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals = sorted(intervals)
        size = len(intervals)
        def binarySearch(nums,left,right):
            mid = (left+right)//2
            print(left,right,mid,nums[mid][0])
            if nums[mid][0]<=newInterval[0]:
                if mid+1<size:
                    if nums[mid+1][0]>newInterval[0]:
                        return mid
                else:
                    return mid
            elif nums[mid][0]>newInterval[0]:
                return binarySearch(nums,left,mid-1)
            else:
                return binarySearch(nums,mid+1,right)
                
        
        #idx = binarySearch(intervals,0,size)
        #print(idx,"index")
        
        #intervals = intervals[:idx+1] + [newInterval] + intervals[idx+1:]
        #print(intervals)
        intervals = self.merge(intervals)
        #print(intervals)
        return intervals