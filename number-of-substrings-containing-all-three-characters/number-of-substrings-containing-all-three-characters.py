class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        size = len(s)
        count = [0,0,0]
        max_ = 0
        low = 0
        
        res = 0
        ans = 0
        
        for high in range(size):
            count[ord(s[high])-ord('a')] += 1
            
            while(low<=high and count[0] and count[1] and count[2]):
                ans += 1
                count[ord(s[low])-ord('a')] -= 1
                low += 1
            
            res += ans
            print(res,ans,count)
        return res
        