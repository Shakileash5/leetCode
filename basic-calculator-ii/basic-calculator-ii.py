class Solution:
    def calculateTwo(self,s):
        operators = ["+","-","*","/"]
        getPrecedense = lambda x: x in ["*","/"]
        isOperator = lambda x: x in operators
        res = ""
        stackOperands = []
        stackOperators = []
        s = s.replace(" ","")
        size = len(s)
        #print(s)
        i = 0
        
        def operate(operator,a,b):
            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == "*":
                return a * b
            elif operator == "/":
                return a // b
            return None
        
        while(i<size):
            if isOperator(s[i]):
                if getPrecedense(s[i]):
                    operatorCurr = s[i]
                    res = ""
                    i+=1
                    while(i<size and not isOperator(s[i])):
                        res += s[i]
                        i+=1
                    numA = stackOperands.pop()
                    numB = int(res)
                    res = ""
                    stackOperands.append(operate(operatorCurr,numA,numB))
                    
                else:
                    stackOperands.append(s[i])
                    i+=1
            else:
                while(i<size and not isOperator(s[i])):
                    res+=s[i]
                    i+=1
                stackOperands.append(int(res))
                res = ""
        #print(stackOperands,stackOperators)
        numA = stackOperands.pop(0)
        i = 0
        if len(stackOperands)==0:
            return numA
        while i<len(stackOperands):
            operator = stackOperands[i]
            i+=1
            numB = stackOperands[i]
            res = operate(operator,numA,numB)
            numA = res
            i+=1
            #print(stackOperands,c,stackOperators)
        return res     
                
    def calculate(self, s: str) -> int:
        
        def calculateOne():
            bufferStr = []
            size = len(s)
            res = ""
            lastNum = ""
            i = 0
            #print(s)

            def isOperator(char):
                if char in ["+","-","*","/"]:
                    return True
                else:
                    return False

            def precedence(char):
                if char in ["/","*"]:
                    return 1
                else:
                    return 0

            def operation(a,b,operator):
                if operator == '+':
                    return int(a)+int(b)
                if operator == '-':
                    return int(a)-int(b)
                if operator == '/':
                    return int(a)//int(b)
                if operator == '*':
                    return int(a)*int(b)

            while (i<size):
                flag = 0
                #print(lastNum)
                if isOperator(s[i]) == False:
                    #bufferStr += s[i]
                    lastNum+=s[i]
                else:
                    operator = s[i]
                    if precedence(s[i]):

                        i+=1
                        nextNum = ""
                        while(i<size and isOperator(s[i])==False):
                            nextNum+=s[i]
                            i+=1
                            flag = 1
                        #print(lastNum,nextNum,operator)
                        result = operation(lastNum,nextNum,operator)
                        lastNum = str(result)
                        #bufferStr.append(lastNum)
                    else:
                        bufferStr.append(lastNum)
                        bufferStr.append(operator)
                        lastNum = ""
                if flag == 0:
                    i+=1
            i = 0
            bufferStr.append(str(int(lastNum)))
            print(bufferStr,lastNum)
            size = len(bufferStr)
            if size == 1:
                return bufferStr[0]
            while(i<size):
                if isOperator(bufferStr[i]) == False:
                    a = bufferStr[i]
                else:
                    b = bufferStr[i+1]
                    result = operation(a,b,bufferStr[i])
                    #print(result)
                    a = str(result)
                    i+=1
                i+=1
            return a
        
        return self.calculateTwo(s)                
                        
                        
                        
                        
                        
                        