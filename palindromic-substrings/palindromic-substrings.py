class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        memo = [[None for j in range(size+2)] for i in range(size+2)]
        
        def isPalindrome(str_):
            sizePali = len(str_)
            left = 0
            right = sizePali - 1
            
            while(left<right):
                if str_[left] != str_[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        
        def isPali(s,left,right):
            if left+1 == right:
                return s[left] == s[right]
            
            if left == right:
                return True
            
            if left>right:
                return False
            
            if memo[left][right] == None:
                memo[left][right] = False
                if s[left] == s[right]:
                    memo[left][right] = isPali(s,left+1,right-1)
                    
            return memo[left][right]
        
        #print(isPali("AhbhA",0,4))
        def naive():
            count = 0
            for i in range(size):
                #print(i)
                for j in range(i+1,size+1):
                    #print(s[i:j])
                    if isPali(s,i,j-1):
                        count += 1
            return count
        #print(naive())
        return naive()