class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        size = len(s)
        maxOnes = 0
        maxZeros = 0
        
        idx = 0
        start = 0
        end = 0
        
        while(end<size):
            if s[end] == '1':
                if s[start] == '0':
                    start = end
                #print(start)
                maxOnes = max(maxOnes,end-start+1)
            else:
                start = end
            end += 1
        
        start = 0
        end = 0
        
        while(end<size):
            if s[end] == '0':
                if s[start] == '1':
                    start = end
                #print(start)
                maxZeros = max(maxZeros,end-start+1)
            else:
                start = end
            end += 1
        
        return maxOnes>maxZeros