class Solution:
    def maxLength(self, arr: List[str]) -> int:
        size = len(arr)
        max_ = [0]
        
        def backtrack(hashMap,length,temp,idx):
            if idx>=size:
                #print(temp,"end")
                max_[0] = max(max_[0],length)
                return
            
            #print(hashMap)
            backtrack(hashMap,length,temp,idx+1)
            
            flag = 0
            localMap = copy.deepcopy(hashMap)
            for i in range(len(arr[idx])):
                if arr[idx][i] not in localMap:
                    localMap[arr[idx][i]] = 1
                else:
                    flag = 1
                    break
            #print("here",arr[idx],"8",temp,flag)
            if flag == 0:
                backtrack(localMap,length+len(arr[idx]),temp+arr[idx],idx+1)
            return
        
        backtrack({},0,'',0)
        return max_[0]