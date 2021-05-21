class Solution:
        def permutations(self,temp,left,right):
            if left>=right:
                self.res.append(temp[:])
                return
            for i in range(left,right+1):
                temp[left],temp[i] = temp[i],temp[left]
                self.permutations(temp,left+1,right)
                temp[left],temp[i] = temp[i],temp[left]
            return
        
        
        def permute(self, nums: List[int]) -> List[List[int]]:
            temp = nums[:]
            size = len(nums)
            self.res = []

            def backtrack(temp,l,r):
                if l>=r:
                    self.res.append(temp[:])
                    #print(temp)
                    #return
                else:
                    for i in range(l,r+1):
                        temp[l],temp[i] = temp[i],temp[l]
                        backtrack(temp,l+1,r)
                        temp[l],temp[i] = temp[i],temp[l]

            #backtrack(temp,0,size-1)
            #print(res)
            self.permutations(temp,0,size-1)
            return self.res
