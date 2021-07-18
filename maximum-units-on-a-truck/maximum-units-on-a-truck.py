class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        size = len(boxTypes)
        
        maxUnits = 0
        boxesLoaded = 0
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        
        for i in range(size):
            if boxesLoaded+boxTypes[i][0]<truckSize:
                boxesLoaded += boxTypes[i][0]
                maxUnits += boxTypes[i][0]*boxTypes[i][1]
                #print(maxUnits,boxTypes[i],"ds",boxesLoaded)
            else:
                noOfBoxes = truckSize - boxesLoaded
                maxUnits += noOfBoxes*boxTypes[i][1]
                #print(maxUnits,boxTypes[i],"s",noOfBoxes,boxesLoaded)
                break
                
        return maxUnits