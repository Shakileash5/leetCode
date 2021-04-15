class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
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