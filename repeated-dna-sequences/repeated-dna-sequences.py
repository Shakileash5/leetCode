class Solution:
    
    def slidingWindowWithHash(self,s):
        size = len(s)
        hashMap = {}
        res = []
        #print(window)
        #print(size)
        if size<=10:
            return res
        for i in range(size):
            window = s[i:i+10]
            #print(hashMap,10+i,i,s[10+i])
            if len(window) == 10:
                if window not in hashMap:
                    hashMap[window] = 1
                else:
                    if hashMap[window] == 1:
                        #print(window)
                        res.append(window)
                    hashMap[window] += 1
        return res
    
    
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        def solutionOne():
            size = len(s)
            hashMap = {}
            repeatingSequence = []        
            for i in range(size):
                subString = s[i:i+10]
                #print(subString)
                if subString in hashMap:
                    if subString not in repeatingSequence:
                        repeatingSequence.append(subString)
                else:
                    hashMap[subString] = 1

            return (repeatingSequence)
        
        return self.slidingWindowWithHash(s)