class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        res = [(0,0)]
        size = len(logs)
        
        nums = []
        for i in range(size):
            nums.append((logs[i][0],0))
            nums.append((logs[i][1],1))
        nums.sort(key=lambda x:x[0])
        #print(nums)
        ans = 0
        alive = 0
        idx = 0
        #print(nums)
        i = 0
        for i in nums:
            if i[1] == 0:
                alive+=1
            elif i[1] == 1:
                alive-=1
            #print(alive,i[0])
            if idx>0 and res[idx][0] == i[0]:
                #print("inside",res,idx)
                if res[idx][1]>alive:
                    res.pop()
                    idx-=1
            if res[idx][1]<alive:
                
                res.append((i[0],alive))
                ans = i[0]
                idx+=1
                print(res)
                
        #print(res)
        return res[idx][0]
            
        
        #for i in range(1,size):
        #    if logs[i-1][1]<logs[i][0]:
        #        nowTotal