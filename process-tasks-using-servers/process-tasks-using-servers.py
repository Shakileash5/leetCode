import heapq
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        
        availableServers = []
        allocatedServers = []
        size = len(servers)
        taskSize = len(tasks)
        res = []
        
        for i in range(size):
            heapq.heappush(availableServers,[servers[i],i])
        #print(availableServers)
        
        def setServersFree(time,allocatedServers,availableServers):
            idx = 0
            timeMin = float('inf')
            #print(allocatedServers,"de")
            while(idx<len(allocatedServers)):
                #print("here",time - (allocatedServers[idx][0]+allocatedServers[idx][1]))
                if (allocatedServers[idx][0])-time<=0:
                    heapq.heappush(availableServers,[allocatedServers[idx][1],allocatedServers[idx][2]])
                    timeMin = min(timeMin,allocatedServers[idx][1])
                    allocatedServers.pop(idx)
                    
                else:
                    idx += 1
            heapq.heapify(allocatedServers) 
            #print(allocatedServers,availableServers)
            return timeMin
        
        #allocatedServers = [[0,2,2,0],[1,3,3,1],[2,3,3,2]]
        #heapq.heapify(allocatedServers)
        #print(allocatedServers)
        #setServersFree(0,allocatedServers,[])
        time = 0
        for i in range(taskSize):
            flag = 0
            #timeMin = setServersFree(time,allocatedServers,availableServers)
            time = max(time,i)
            if len(availableServers)==0:
                time = allocatedServers[0][0]
            
            while(len(allocatedServers) and time>=allocatedServers[0][0]):
                temp = heapq.heappop(allocatedServers)
                heapq.heappush(availableServers,[temp[1],temp[2]])
                
            
            freeServer = heapq.heappop(availableServers)
            heapq.heappush(allocatedServers,[time+tasks[i],freeServer[0],freeServer[1]])
            res.append(freeServer[1])
            #time += 1
        
        return res
            
        
        