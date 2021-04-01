class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        postFix = []
        
        operators = ['+','-','*','/']
        
        for i in tokens:
            #print(postFix)
            if i not in operators:
                postFix.append(i)
            else:
                val1 = int(postFix.pop())
                val2 = int(postFix.pop())
                if i == "+":
                    val2 = val2+val1
                if i == "-":
                    val2 = val2-val1
                if i == "*":
                    val2 = val1*val2
                if i == "/":
                    val2 = val2/val1
                
                postFix.append(int(val2))
        
        return postFix[0]
                    