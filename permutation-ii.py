# https://leetcode.com/problems/permutations-ii/
# Problem Description

# Solution
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        temp = nums[:]
        size = len(nums)
        res = []
        
        def backtrack(temp,l,r):
            if l>=r:
                if temp not in res:
                    res.append(temp[:])
                #print(temp)
                #return
            else:
                for i in range(l,r+1):
                    temp[l],temp[i] = temp[i],temp[l]
                    backtrack(temp,l+1,r)
                    temp[l],temp[i] = temp[i],temp[l]
        
        backtrack(temp,0,size-1)
        #print(res)
        return res

#solution
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        temp = []
        size = len(nums)
        res = []
        n = len(nums)
        #self.res = []
        visited = set()
        ele = []
        
        def backtrack(temp,idx, visited):
            if len(temp) == size:
                if temp not in res:
                    res.append(temp)
                return
            else:
                for i in range(size):
                    if i != idx and i not in visited:
                        visited.add(i)
                        #temp.append(nums[i])
                        #print(nums[i])
                        backtrack(temp+[nums[i]],i,visited)
                        #temp.pop()
                        visited.discard(i)
                return

        
        for i in range(size):
			# start from each element in the array
            visited.add(i)
            ele.append(nums[i])
            backtrack([nums[i]],i, visited)
            ele.pop()
            visited.discard(i)

        return res