class Solution:
    def permutationsUnique(self,temp,left,right):
        if left>=right:
            #print(temp,self.res)
            if temp not in self.res:
                self.res.append(temp[:])
                return
        for i in range(left,right+1):
            temp[left],temp[i] = temp[i],temp[left]
            self.permutationsUnique(temp,left+1,right)
            temp[left],temp[i] = temp[i],temp[left]
        
        return 
        
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        temp = []
        size = len(nums)
        res = []
        n = len(nums)
        self.res = []
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

        
        """for i in range(size):
			# start from each element in the array
            visited.add(i)
            ele.append(nums[i])
            backtrack([nums[i]],i, visited)
            ele.pop()
            visited.discard(i)"""
        
        self.permutationsUnique(nums[:],0,size-1)
        return self.res