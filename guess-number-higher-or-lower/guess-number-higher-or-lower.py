# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        result = [0]
        def binarySearch(left,right):
            num = (left+right)//2
            res = guess(num)
            #print(res,num)
            if res == 1:
                if binarySearch(num+1,right):
                    return True
            elif res == -1:
                if binarySearch(left,num-1):
                    return True
            elif res == 0:
                result[0] = num
                return True
            return
                
        
        #guessNum = random.randint(0,n)
        binarySearch(0,n)
        
        return result[0]
            