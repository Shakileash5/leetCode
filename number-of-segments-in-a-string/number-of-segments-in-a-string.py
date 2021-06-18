class Solution:
    def countSegments(self, s: str) -> int:
        size = len(s)
        splits = 0
        flag = 0
        for i in range(size):
            if s[i] != ' ':
                if flag == 0:
                    flag = 1
                    splits += 1
            else:
                flag = 0
        
        return splits