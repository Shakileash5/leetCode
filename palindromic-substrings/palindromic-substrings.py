class Solution:
    def countSubstrings(self, s: str) -> int:
        
        size = len(s)
        count = 0
        hashMap = {}
        
        def isPalindrome(string):
            size = len(string)
            left = 0
            right = size - 1
            while(left<right):
                if string[left] != string[right]:
                    return False
                left+=1
                right-=1
            return True
        
        def bruteForce():
            for i in range(size):
                for j in range(i,size):
                    subStr = s[i:j+1]
                    subSize = len(subStr)
                    #print(subStr)
                    flag = 0
                    if subSize%2==0:
                        if hashMap.get(subStr[1:subSize-1],0):
                            flag = 1
                            if subStr[0] == subStr[subSize-1]:
                                count+=1
                    elif subSize%2==1 and subSize>=3:
                        if hashMap.get(subStr[1:subSize-1],0):
                            flag = 1
                            if subStr[0] == subStr[subSize-1]:
                                count+=1
                    if flag ==0 and isPalindrome(subStr):
                            hashMap[subStr] = 1
                            count+=1
        if s is None or s.strip() == '':
            return 0
        
        totalPal = 0
        
        for i in range (0,len(s)):
            
            # for odd len pal, single char at center 
            totalPal += self.countPal(s,i,i)
            
            # for even Len pal, consecutive char at center
            totalPal += self.countPal(s,i,i+1)
            
        return totalPal
        
    def countPal(self,s,lo,hi):
        count = 0
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
            count +=1   # each occurance is one count 
        #print("Count is : ", count)    
        return count # s[lo+1,hi]
                
            