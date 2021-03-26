class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        n = n + 1
        output = [None] * (n+1)
        i = 0
        while i<len(output):
            print(i,output)
            if None not in output:
                break
            else:
                if i == 0:
                    output[i] = 0
                if i == 1:
                    output[i] = 1
                if 2*i <= n and 2 <= 2*i:
                    print("idx",2*i,output[i])
                    output[2*i] = output[i]
                if 2 <= 2*i+1 and 2*i+1 <= n:
                    print("idx 2",2*i+1,output[i] + output[i+1])
                    output[2*i+1] = output[i] + output[i+1]
            i += 1
        return max(output[:n])
