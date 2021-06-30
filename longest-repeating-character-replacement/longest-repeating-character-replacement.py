class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        resMax = 0 
        
        def chrReplacementUtil(char,k):
            left = 0
            right = 0
            diffChar = 0
            max_ = 0
            
            while(right<size):
                if s[right] != char:
                    diffChar += 1
                while(diffChar>k):
                    if s[left] != char:
                        diffChar -= 1
                    left += 1
                max_ = max(max_,right-left+1)    
                right += 1
            
            return max_
        
        for i in range(26):
            lowerChar = chrReplacementUtil(chr(i+ord('a')),k)
            upperChar = chrReplacementUtil(chr(i+ord('A')),k)
            resMax = max(resMax,max(lowerChar,upperChar))
        return resMax