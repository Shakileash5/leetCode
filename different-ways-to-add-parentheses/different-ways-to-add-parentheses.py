class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        size = len(expression)
        operands = set(["+","-","*"])

        def divideAndConquere(string):
            if ("+" not in string and "-" not in string and "*" not in string):
                return [int(string)]
            
            sizeStr = len(string)
            res = []   
            #print(string,sizeStr)
            for i in range(sizeStr):
                if (string[i] in operands):
                    #print("in")
                    left = divideAndConquere(string[:i])
                    right = divideAndConquere(string[i+1:])
                    #print(left,right)
                    for l in left:
                        for r in right:
                            print(str(l)+str(i)+str(r))
                            res.append(eval(str(l)+str(string[i])+str(r)))
                            #print(res)
            return res
        
        return divideAndConquere(expression)
                    