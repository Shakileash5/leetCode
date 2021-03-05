class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = len(s)
        temp = s.split()
        print(temp)
        if temp == []:
            return  0

        else:
            res = temp[-1].strip()
            return len(res) 
        
        
        