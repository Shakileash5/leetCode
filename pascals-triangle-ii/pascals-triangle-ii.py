class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascalsTriangle = []
        for i in range(1,rowIndex+2):
            idx = 0
            for j in range(i):
                if j == 0:
                    pascalsTriangle.append([1])
                elif j == i-1:
                    pascalsTriangle[i-1].append(1)
                else:
                    if i >2:
                        val = pascalsTriangle[i-2][idx]+pascalsTriangle[i-2][idx+1]
                        #print(val,idx,pascalsTriangle[i-2])
                        idx+=1
                        pascalsTriangle[i-1].append(val)
                        
        return(pascalsTriangle[-1])