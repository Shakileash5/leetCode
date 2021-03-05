# https://leetcode.com/problems/group-anagrams/
# Problem Description

# Solution TestCases 111/114
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashStack = {}
        visited = set()
        size = len(strs)
        res = []
        idx = 0
        
        for i in range(size):
            
            if i not in visited:
                sizeSelectedString = len(strs[i])
                res.append([strs[i]])
                idx+=1
                for k in range(sizeSelectedString):
                    if strs[i][k] not in list(hashStack.keys()):
                        hashStack[strs[i][k]] = [1,0]
                    else:
                        hashStack[strs[i][k]][0]+=1
                #print(hashStack,i,"st")
                keys = list(hashStack.keys())
                for j in range(i+1,size):
                    flag = 0
                    sizeCompareString = len(strs[j])
                    if sizeSelectedString == sizeCompareString:
                        for k in range(sizeCompareString):
                            #print(strs[j][k],keys,strs[j][k] in keys)
                            if strs[j][k] in keys:
                                hashStack[strs[j][k]][1] +=1
                            else:
                                #print("here")
                                flag = 1
                        #print("tackle",hashStack,strs[j],flag)
                        if flag == 0:        
                            for key in keys:
                                if hashStack[key][0] == hashStack[key][1]:
                                    hashStack[key][1] = 0
                                else:
                                    hashStack[key][1] = 0
                                    flag = 1
                            if flag == 0:
                                visited.add(j)
                                res[idx-1].append(strs[j])
                        else:
                            for key in keys:
                                hashStack[key][1] = 0
                                
                hashStack = {}
        #print(res)
        return res
                    
#Optimized Solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashStack = {}
        visited = set()
        size = len(strs)
        #res = []
        idx = 0
        
        for i in range(size):   
            
            temp = strs[i]
            temp = "".join(sorted(temp))
            
            if temp in list(hashStack.keys()):
                hashStack[temp].append(strs[i])
            else:
                hashStack[temp] = [strs[i]]
            
        #print(hashStack.values())   
        return list(hashStack.values())
                    
                