class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitList = []
        size = len(words)
        
        for word in words:
            bit = 0
            for char in word:
                charIdx = ord(char)-ord('a')
                bit = 1<<charIdx | bit #set ith bit
                #print(char,charIdx,bit)
            #print(word,bit)
            bitList.append(bit)
        maxLength = 0
        #print(words,bitList)
        for i in range(size):
            for j in range(i+1,size):
                if bitList[i] & bitList[j] == 0:
                    length = len(words[i]) * len(words[j])
                    maxLength = max(maxLength,length)
                
        return maxLength