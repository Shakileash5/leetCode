class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        size = len(nums)
        def naive():
            nums_ = sorted(nums)
            count = 0
            end = -1
            #print(nums_)
            for i in range(size):
                count_ = 1
                start = i
                end = i+1
                while(end<size and (nums_[start]+1 == nums_[end] or nums_[start] == nums_[end])):
                    if nums_[start] != nums_[end]:
                        count_+=1
                    end+=1
                    start+=1
                    #print("here")
                #print(count_)
                count = max(count,count_)
        
        def backtrack(idx,temp):
            if idx>=size:
                #temp.sort()
                #print(temp)
                self.count = max(self.count,len(temp))
                return
            backtrack(idx+1,temp)
            if temp == [] or abs(temp[-1]-nums[idx])==1:
                backtrack(idx+1,temp+[nums[idx]])
        #nums.sort()
        #self.count = 0
        #backtrack(0,[])
        
        def hashing():
            hashMap = {}
            count = 0
            for i in nums:
                hashMap[i] = 1
            for key in nums:
                start = -1
                count_ = 1
                if key-1 not in hashMap:
                    start = key
                    while start+1 in hashMap:
                        start+=1
                        count_+=1
                    count = max(count,count_)
                    #print(count_)
            return count
        return hashing()