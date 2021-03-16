class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        def binaryToDecimal(binary): 
            binary = int(binary)
            binary1 = binary 
            decimal, i, n = 0, 0, 0
            while(binary != 0): 
                dec = binary % 10
                decimal = decimal + dec * pow(2, i) 
                binary = binary//10
                i += 1
            return(decimal)  
        
        if n<=0:
            return 
        arr = []
        arr.append("0")
        arr.append("1")
        
        i = 2
        j = 0
        
        while True:
            
            if i>= 1<<n:
                break
            
            for j in range(i-1,-1,-1):
                arr.append(arr[j])
            #print("here",arr)
            for j in range(i):
                arr[j] = "0" + arr[j]
            
            for j in range(i,2*i):
                arr[j] = "1" + arr[j]
            
            #print(arr,i)
            
            i = i<<1
        res = []
        for i in range(len(arr)):
            res.append(binaryToDecimal(arr[i]))
        return(res)
        
                
        