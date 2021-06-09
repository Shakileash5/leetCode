class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num_ = list(map(int,list(str(num))))
        size = len(num_)
        swap = 1
        idx = 0
        maxArr = [(num_[size-1],size-1)]
        for i in range(size-2,-1,-1):
            if num_[i] > maxArr[-1][0]:
                maxArr.append((num_[i],i))
            else:
                maxArr.append(maxArr[-1])
        maxArr = maxArr[::-1]
        #print(num_,maxArr)
        
        while(swap):
            idx = 0
            swap = 0
            while(idx<size):
                if maxArr[idx][0] != num_[idx] and maxArr[idx][1] != idx:
                    num_[idx],num_[maxArr[idx][1]] = num_[maxArr[idx][1]],num_[idx]
                    break
                idx += 1
            swap = 0
        #print(num_)
        return int(''.join(list(map(str,num_))))