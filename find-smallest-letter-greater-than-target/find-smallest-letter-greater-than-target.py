class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        nextSmallest = None
        nextGreatest = None
        smallest = None
        greatest = None
        
        
        for i in letters:
            if i>target:
                #print('here')
                if nextSmallest == None:
                    nextSmallest = i
                elif nextSmallest>i:
                    nextSmallest = i
            if i<target:
                if nextGreatest == None:
                    nextGreatest = i
                elif nextGreatest>i:
                    nextGreatest = i
        
        if nextSmallest!=None:
            return nextSmallest
        return nextGreatest