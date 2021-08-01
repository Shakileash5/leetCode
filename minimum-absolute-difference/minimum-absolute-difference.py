class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        size = len(arr)
        min_ = 100000
        res = []
        arr.sort()
        print(arr)
        for i in range(size-1):
            if min_>abs(arr[i]-arr[i+1]):
                min_ = abs(arr[i]-arr[i+1])
                res = [[arr[i],arr[i+1]]]
            elif min_ == abs(arr[i]-arr[i+1]):
                res.append([arr[i],arr[i+1]])
            #print(min_,res,i,arr[i],arr[i+1])
        return res