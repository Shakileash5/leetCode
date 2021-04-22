class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        size = len(num)
        #num1 = int(num[0])
        #num2 = int(num[1])
        fl1 = [0]
        fl2 = [0]
        def backtrack(idx,num1,num2):
            if idx>=(size):
                return True
            
            for i in range(idx,size):
                val = num[idx:i+1]
                #print(num1,num2,"val::",val,"idx",i)
                if len(val)>1 and val[0] == "0":
                    continue
                val = int(val)
                if (num1+num2) == val:
                    num1 = num2
                    num2 = val
                    if backtrack(i+1,num1,num2) == True:
                        return True
                    else:
                        return False
                            
            return False
        
        
        for i in range(size//2):
            for j in range(i+1,size-1):
                num1 = num[:i+1]
                if len(num1)>1 and num1[0]=="0":
                    continue
                num2 = num[i+1:j+1]
                if len(num2)>1 and num2[0]=="0":
                    continue
                #print(num1,num2,i,j)
                if backtrack(j+1,int(num1),int(num2))==True:
                    return True
        
        return False