class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        invalidTransactions = []
        invalidSet = set()
        size = len(transactions)
        for i in range(size):
            val = transactions[i].split(",")
            #print(val)
            transactions[i] = val
        #print(transactions)
        idx = 0
        
            
        
        for i in range(0,len(transactions)):
            valid = 1
            for j in range(i):
                if transactions[j][0] == transactions[i][0] and abs(int(transactions[i][1])-int(transactions[j][1]))<=60 and transactions[j][3]!=transactions[i][3]:
                    print("abort",transactions[i],transactions[j],i,j,int(transactions[i][1])-int(transactions[j][1]))
                    if j == i:
                        continue
                    if j not in invalidSet:
                        invalidTransactions.append(','.join(transactions[j]))
                        invalidSet.add(j)
                    if i not in invalidSet:
                        invalidTransactions.append(','.join(transactions[i]))
                        invalidSet.add(i) 
                    valid = 0
            if valid == 1:
                if int(transactions[i][2])>1000:
                    print("above1000",transactions[i])
                    if i not in invalidSet:
                        invalidTransactions.append(','.join(transactions[i]))
                        invalidSet.add(i)  
        return(invalidTransactions)
                    
                    
                    