class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1:
            return True
        
        
        def iSValidPalindrome(string,size):
                if size==1:
                    return True
                mid = size//2
                str1,str2 = string[:mid],string[-mid:]
                str2 = str2[::-1]
                if str1==str2:
                    return True
                return False
        
        #print(iSValidPalindrome("abbcrbba",8))
        def removeExtras(string):
            resString = ""
            for i in string:
                if i>="a" and i<="z" or i>="A" and i<="Z" or i>="0" and i<="9":
                    resString+=i.lower()
            
            return resString
        string = removeExtras(s)
        print(string)
        return iSValidPalindrome(string,len(string))