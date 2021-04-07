class Solution:
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
        
        table = seiveMethod(n)
        res = []
        print("fe",table,n)
        for i in range(2,n):
            if table[i]:
                #print(i,end=' ')
                res.append(i)
        return len(res)