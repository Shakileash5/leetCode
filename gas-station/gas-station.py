class Solution:
    def gasStation(self,gas,cost):
        size = len(gas)
        
        def canReach(idx):
            if gas[idx]<cost[idx]:
                return False
            start = idx
            gasAvailable = gas[idx]
            gasAvailable -= cost[idx]
            idx = (idx+1)%size
            while start!=idx:
                gasAvailable += gas[idx]
                if gasAvailable<cost[idx]:
                    return False
                gasAvailable -= cost[idx]
                idx = (idx+1)%size
            return True
        
        #res = canReach(3)
        for i in range(size):
            if canReach(i):
                return i
        return -1
            
            
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        def travel(start,gas,cost,size)->bool:
            
            gasAvailable = gas[start]
            gasAvailable -= cost[start]
            idx = start+1
            if gasAvailable<0:
                return False
            #print(gasAvailable)
            if idx == size:
                idx=0
            while(idx!=start):
                gasAvailable += gas[idx]
                gasAvailable -= cost[idx]
                if gasAvailable <0:
                    return False
                #print(gasAvailable,idx)    
                idx+=1
                if idx==size:
                    idx = 0
            
            return True
        size = len(gas)
        #res = travel(4,gas,cost,size)
        #for i in range(size):
        #    res = travel(i,gas,cost,size)
        #    if res == True:
        #        return i
        
        #return -1
        
        return self.gasStation(gas,cost)