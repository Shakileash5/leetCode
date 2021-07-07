class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        size = len(palindrome)
        flag = 0
        mid = size//2
        res = ''
        flagPali = False
        
        if size%2 == 1:
            flag = 1
        
        for i in range(size):
            #print(i,mid)
            if flag == 1 and i == mid:
                res += palindrome[i]
            else:
                if flagPali == False and palindrome[i] != 'a':
                    res += 'a'
                    flagPali = True
                elif flagPali == False and i+1==size and palindrome[i] == 'a':
                    res += 'b'
                    flagPali = True
                else:
                    res += palindrome[i]
        
        if flagPali:
            return res
        return ''
            
            