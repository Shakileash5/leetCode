class Solution:
    def partitionTwo(self,s):
        size = len(s)
        res = []
        def isPalindrome(s):
            mid = len(s)
            if s[:mid] == s[-mid:][::-1]:
                return True
            return False
        
        def backtrack(idx,temp):
            if idx>=size:
                res.append(temp)
                return
            for i in range(idx,size):
                subStr = s[idx:i+1]
                if isPalindrome(subStr):
                    backtrack(i+1,temp+[subStr])
            return
        backtrack(0,[])
        return res
    
    def partition(self, s: str) -> List[List[str]]:
        
        size = len(s)
        allPartitions = []
        def iSValidPalindrome(string,size):
                if size==1:
                    return True
                mid = size//2
                str1,str2 = string[:mid],string[-mid:]
                str2 = str2[::-1]
                if str1==str2:
                    return True
                return False
        
        def backtrack(idx,partitions):
            if idx>=size:
                #print(partitions,"pa")
                partSize = 0
                for i in partitions:
                    partSize+=len(i)
                if partSize == size:
                    allPartitions.append(partitions)
                return
            
            for i in range(idx,size):
                #for j in range(i+1,size+1):
                    string = s[idx:i+1]
                    #print(string)
                    if iSValidPalindrome(string,len(string)):
                        
                        backtrack(i+1,partitions+[string])
            return
        
        #backtrack(0,[])
        #return allPartitions
        return self.partitionTwo(s)