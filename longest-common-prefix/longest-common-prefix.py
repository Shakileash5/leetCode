class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def naiveSolution():
            res = ""
            i,j,k = 0,0,0
            size = len(strs)
            #print(size,strs)
            if size == 0:
                return res
            if len(strs[0]) == 0:
                    return res
            size1 = len(strs[0])
            while True:
                flag = 0
                if i>=size1:
                    break
                r = strs[0][i]
                #print(j,size,strs[j])
                if i>=len(strs[j]) or r != strs[j][i]:
                    flag = 1
                    break
                if j==(size-1):
                    i+=1
                    j = 0
                    res +=r
                else:
                    j+=1
        
        def solutionWithPtr():
            idx = 0
            resPrefix = ""
            size = len(strs)
            if size==0:
                return ""
            while True:
                stackIdx = 0
                flag = 0
                if idx<len(strs[0]):
                    tempStr = strs[0][idx]
                    while(stackIdx<size):
                        if idx>=len(strs[stackIdx]) or idx<len(strs[stackIdx]) and strs[stackIdx][idx] != tempStr:
                            flag = 1
                            #print("here")
                            break
                        stackIdx+=1
                else:
                    #print(idx,resPrefix,"fe")
                    flag = 1
                if flag == 1:
                    break
                resPrefix+=tempStr
                idx+=1
            return resPrefix
                
        
        #print()
        #return res
        return solutionWithPtr()