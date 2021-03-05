# https://leetcode.com/problems/multiply-strings/
# Problem Description

# Solution
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        size1 = len(num1)
        size2 = len(num2)
        
        tens1 = 10**(size1-1)
        tens2 = 10**(size2-1)
        
        digit1 = 0
        digit2 = 0
        
        idx = 0
        maxSize = max(size1,size2)
        
        while idx<maxSize:
            
            if idx<size1:
                digit1 += (ord(num1[idx]) - ord('0'))*(tens1)
                tens1//=10
                #digit1 += temp*tens
            
            if idx<size2:
                digit2 += (ord(num2[idx]) - ord('0'))*tens2
                tens2//=10
            
            #tens*=10
            idx+=1
        
        #print(digit1,digit2)
        return str(digit1*digit2)