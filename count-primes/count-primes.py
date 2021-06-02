class Solution:
    def countPrimesTwo(self,n):
        if n == 2:
            return 0
        
        table = [True for _ in range(n+1)]
        
        def seiveMethod(table):
            i = 2
            while(i*i<=n):
                if table[i]:
                    for j in range(i*i,n,i):
                        table[j] = False
                i+=1
            return
        seiveMethod(table)
        count = 0
        for i in range(2,n):
            if table[i]:
                count+=1
        return count
    
    def countPrimes(self, n: int) -> int:
        if n==2:
            return 0
        def seiveMethod(num):
            seiveTable = [True for _ in range(num+1)]
            i = 2
            while(i*i<=num):
                if seiveTable[i]:
                    print(i)
                    for j in range(i*i,num+1,i):
                        seiveTable[j] = False
                i+=1
            return(seiveTable)
        
        def solutionOne():
            table = seiveMethod(n)
            res = []
            print("fe",table,n)
            for i in range(2,n):
                if table[i]:
                    #print(i,end=' ')
                    res.append(i)
            return len(res)
        return self.countPrimesTwo(n)