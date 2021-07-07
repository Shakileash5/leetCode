class Solution:
    def longestPalindrome(self, s: str) -> int:
        size = len(s)
        
        hashMap = {}
        countUnique = 0
        totalKey = 0
        keys = []
        
        for i in range(size):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
                countUnique += 1
                totalKey += 1
            else:
                if hashMap[s[i]]<=1:
                    countUnique -= 1
                    keys.append(s[i])
                hashMap[s[i]] += 1
                

        #print(countUnique,totalKey)
        palindrome = 0
        flag = 0
        for key in keys:
            if hashMap[key]%2 == 1:
                #print("here")
                if flag == 0:
                    flag = 1
                    palindrome += hashMap[key]
                else:
                    palindrome += hashMap[key] - 1
            else:
                palindrome += hashMap[key]
            #print(palindrome,key,hashMap)
        if flag == 0 and countUnique>0:
            palindrome += 1

        return palindrome
            
        