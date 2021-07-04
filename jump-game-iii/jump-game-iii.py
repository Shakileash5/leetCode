class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        size = len(arr)
        visited = [False for i in range(size+1)]
        def recur(idx):
            
            if arr[idx] == 0:
                return True
            if visited[idx]:
                return False
            visited[idx] = True
            if 0 <= idx + arr[idx] < size:
                if recur(idx+arr[idx]):
                    return True
            if 0<= idx-arr[idx] < size:
                if recur(idx-arr[idx]):
                    return True
            
            return False
        
        return recur(start)