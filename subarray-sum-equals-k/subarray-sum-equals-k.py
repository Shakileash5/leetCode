class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        size = len(nums)
        count = 0
        
        right = 1
        sum_ = 0
        hashMap = {}
        hashMap[0] = 1
        #nums[0]
        #if sum_ == k:
        #    count+=1
        def nonNegativeSol():
            for i in range(0,size):
                left = 0
                subArray = nums[left:i+1]

                sum_+=nums[i]
                print("st",subArray,sum_,left,i)
                if sum_ == k:
                    count+=1
                if sum_>k:
                    while(sum_>k and left<i):
                        sum_ -=nums[left]
                        left+=1
                    print("out",sum_,left)
                    if sum_==k:
                        count+=1
                print(count,nums[left:i+1],sum_)

            print("final",count)
        
        #prefixSum Solution
        for i in range(size):
            sum_ += nums[i]
            if sum_-k in hashMap:
                count+= hashMap[sum_-k]
            hashMap[sum_] = hashMap.get(sum_,0)+1
        
        return count
                    
        