class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        flag = 0
        size = len(arr)
        didAssend = False
        
        for i in range(1,size):
            if flag == 0:
                if arr[i]==arr[i-1]:
                    print("here")
                    return False
                if arr[i]<arr[i-1]:
                    flag = 1
                else:
                    didAssend = True
            else:
                if arr[i]>=arr[i-1]:
                    return False
        if flag and didAssend:
            return True
        return False
            