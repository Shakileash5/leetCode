class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashMap = {5:0,10:0,20:0}
        size = len(bills)
        
        for i in range(size):
            if bills[i] == 5:
                hashMap[5] += 1
            if bills[i] == 10:
                hashMap[10] += 1
                print(hashMap,bills[i])
                if hashMap[5]>0:
                    hashMap[5] -= 1
                else:
                    return False
            if bills[i] == 20:
                flag = 0
                #print(hashMap,bills[i])
                if hashMap[10]>0:
                    if hashMap[5]>0:
                        hashMap[5]-=1
                        hashMap[10]-=1
                        flag = 1
                if flag == 0 and hashMap[5]>=3:
                    hashMap[5] -= 3
                    flag = 1
                if flag == 0:
                    return False
        return True
        