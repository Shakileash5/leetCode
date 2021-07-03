class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        strRow1 = "qwertyuiop"
        strRow2 = "asdfghjkl"
        strRow3 = "zxcvbnm"
        size = len(words)
        
        hashMap = {}
        res = []
        
        for i in strRow1:
            hashMap[i] = 1
        for i in strRow2:
            hashMap[i] = 2
        for i in strRow3:
            hashMap[i] = 3
            
        for i in range(size):
            start = hashMap[words[i][0].lower()]    
            flag = 0
            for j in range(len(words[i])):
                if hashMap[words[i][j].lower()] != start:
                    flag = 1
                    break
            if flag == 0:
                res.append(words[i])
        
        return res