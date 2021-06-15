import random
class Solution:
    def binaryWithCostTwo(self,n):
        memo = [[None for i in range(n+1)] for j in range(n+1)]
        def recur(left,right):
            if right - left == 1:
                return left
            if right == left:
                return 0
            if memo[left][right] == None:
                min_ = float('inf')
                for i in range(left+1,right):
                    val = i + max(recur(left,i-1),recur(i+1,right))
                    min_ = min(min_,val)
                memo[left][right] = min_
                return min_
            else:
                return memo[left][right]
                
        
        return recur(0,n)
    
    def getMoneyAmount(self, n: int) -> int:
        
        self.amount = 0
        self.start = 0
        res = float("inf")
        def binarySearchWithCost(left,right,val,costPath):
            
            if left>right:
                temp = sum(costPath)-costPath[-1]
                self.amount = max(self.amount,temp)
                print(temp,val,costPath)
                return
            if self.start==0:
                mid = val
                #print("here")
                self.start+=1
            else:
                mid = random.randint(left,right)
                
            #print(mid,left,right,"cost:::",costPath,sum(costPath))
            binarySearchWithCost(left,mid-1,val,costPath+[mid])
            #print("cost::",cost)
            binarySearchWithCost(mid+1,right,val,costPath+[mid])
            
            return
        #for i in range(1,n+1):
        #    self.start = 0
        #    binarySearchWithCost(0,n,i,[])
        #    print(self.amount,i)
        #    res = min(self.amount,res)
        #    self.amount = 0
        @cache
        def payToGuess(left,right):
            if right - left == 1:
                return left
            
            if left == right:
                return 0
            
            min_ = float("inf")
            for i in range(left+1,right):
                leftVal = i + payToGuess(left,i-1)
                rightVal = i + payToGuess(i+1 , right)
                min_ = min(min_,max(leftVal,rightVal))
            
            return min_
        
        #return payToGuess(0,n)
        return self.binaryWithCostTwo(n)  