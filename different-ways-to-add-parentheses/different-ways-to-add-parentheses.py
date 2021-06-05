class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        size = len(expression)
        isOperand = lambda x : x in ["+","-","*","/"]
        
        def recur(string):
            if ("+" not in string and "-" not in string and "*" not in string):
                return [int(string)] 
            res = []
            for i in range(len(string)):
                if isOperand(string[i]):
                    left = recur(string[:i])
                    right = recur(string[i+1:])
                    for l in left:
                        for r in right:
                            #print(left,string[i],right)
                            res.append(eval(str(l)+string[i]+str(r)))
                    
            return res
        
        return recur(expression)
        