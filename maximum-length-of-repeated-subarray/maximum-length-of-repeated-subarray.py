class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        size1 = len(nums1)
        size2 = len(nums2)
        
        #print(hashMap)
        def naive():
            max_ = 0
            hashMap = {}
            for i in range(size2):
                if nums2[i] not in hashMap:
                    hashMap[nums2[i]] = [i]
                else:
                    hashMap[nums2[i]].append(i)
            for i in range(size1):
                start = i
                end1 = i
                temp = end1
                if nums1[i] not in hashMap:
                    continue
                for j in range(len(hashMap[nums1[i]])):
                    #print(j,hashMap[nums1[i]][j],"here")
                    if j > 0 and hashMap[nums1[i]][j] == hashMap[nums1[i]][j-1]+1:
                        continue
                    end1 = temp
                    end2 = hashMap[nums1[i]][j]
                    #print(j,end1,"indsd")
                    while(end1<size1 and end2<size2 and nums1[end1] == nums2[end2]):
                        max_ = max(max_,end1-start+1)
                        #print(nums1[end1],nums2[end2],"dd",end=' ')
                        end1 += 1
                        end2 += 1
                    #print()
            return max_
        
        dp = [[None for i in range(max(size1,size2)+1)] for j in range(max(size1,size2)+1)]
        count = [0]
        
        def recur(idx1,idx2):
            if idx1<=0 or idx2<=0:
                return 0
            if dp[idx1][idx2] == None:    
                res1 = recur(idx1,idx2-1)
                res2 = recur(idx1-1,idx2)
                if nums1[idx1-1] == nums2[idx2-1]:
                    dp[idx1][idx2] = 1 + recur(idx1-1,idx2-1)
                    count[0] = max(count[0],dp[idx1][idx2])
                    return dp[idx1][idx2]
                dp[idx1][idx2] = 0
                return dp[idx1][idx2]
            else:
                return dp[idx1][idx2]
        #recur(size1,size2)
        #return count[0]
        N,M = len(nums1),len(nums2) 
        dp = [[0]*(M+1) for _ in range(N+1)]
        r = 0
        for i in range(1,N+1):
            for j in range(1,M+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
        
            r = max(r,max(dp[i]))
        
        return r    
        