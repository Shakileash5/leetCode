class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        hashMap = {}
        max_ = max(len(s1),len(s2))
        dp = [[None for i in range(max_+1)] for j in range(max_+1)]
        #print(len(dp),len(dp[0]))
        def backtrack(idx1,idx2,idx3,s1,s2,s3,temp):
            if idx3>=len(s3):
                if temp==s3 and idx1>=len(s1) and idx2>=len(s2):
                    print(temp,s3,temp==s3,idx1,idx2)
                    return True
                return
            #print(idx1,idx2)
            res = False
            res2 = False
            if dp[idx1][idx2] == None:
                if idx1<len(s1):
                    res = backtrack(idx1+1,idx2,idx3+1,s1,s2,s3,temp+s1[idx1])
                    #hashMap[(idx1,idx2,idx3)] = res
                    if res:
                        return True
                if idx2<len(s2):
                    res2 = backtrack(idx1,idx2+1,idx3+1,s1,s2,s3,temp+s2[idx2])

                    if res2:
                        return True
                dp[idx1][idx2] = res or res2
            else:
                return dp[idx1][idx2]
        @cache
        def backtrack2(idx1,idx2,idx3,s1,s2,s3,temp):
            if idx3>=len(s3):
                if temp==s3 and idx1>=len(s1) and idx2>=len(s2):
                    print(temp,s3,temp==s3,idx1,idx2)
                    return True
                return
            if idx1<len(s1) and idx3<len(s3) and s1[idx1] == s3[idx3]:
                res = backtrack2(idx1+1,idx2,idx3+1,s1,s2,s3,temp+s1[idx1])
                if res:
                    return True
            if idx2<len(s2) and idx3<len(s3) and s2[idx2] == s3[idx3]:
                resN = backtrack2(idx1,idx2+1,idx3+1,s1,s2,s3,temp+s2[idx2])
                if resN:
                    return True
                
        return backtrack2(0,0,0,s1,s2,s3,"")