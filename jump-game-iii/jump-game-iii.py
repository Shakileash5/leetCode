class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        size = len(arr)
        
        visited = [False for i in range(size)]
        def dfs(idx):
            if arr[idx] == 0:
                return True
        
            visited[idx] = True
            if arr[idx]+idx<=size-1 and visited[arr[idx]+idx]==False:
                if dfs(arr[idx]+idx):
                    return True
            if idx-arr[idx]>=0 and visited[idx-arr[idx]]==False:
                if dfs(idx-arr[idx]):
                    return True
            
            return False
        
        return dfs(start)