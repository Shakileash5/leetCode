class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        self.n = len(grid)
        self.dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        self.hashMap = {}
        self.areaArray = {}
        self.id = 0
        
        self.dfs(grid) 
        max_area = 0

        
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 0:
                    visitedId = set()
                    size = 1
                    for a, b in self.dirs:
                        if -1 < i+a < self.n and -1 < j+b < self.n:
                            if (i+a, j+b) in self.hashMap and self.hashMap[(i+a, j+b)] not in visitedId:
                                visitedId.add(self.hashMap[(i+a, j+b)])
                                size += self.areaArray[self.hashMap[(i+a, j+b)]]
                    max_area = max(max_area, size)
        
        if not max_area:
            return self.n*self.n
            
        return max_area
    
    
    def dfs(self, array):
        
        def DFSUtils(i,j,visited):
            visited.add((i,j))
            self.hashMap[(i,j)] = self.id
            for a, b in self.dirs:
                if -1 < i + a < self.n and -1 < j + b < self.n:
                    if array[i+a][j+b] == 1:
                        if (i+a, j+b) not in visited:
                            DFSUtils.count += 1
                            DFSUtils(i+a, j+b, visited)
            return
        
                
        def DFS():
            max_area = 0
            visited = set()
            for i in range(self.n):
                for j in range(self.n):
                    if array[i][j] == 1 and (i,j) not in visited:
                        self.id += 1
                        DFSUtils.count = 0
                        DFSUtils(i, j, visited)
                        DFSUtils.count += 1
                        self.areaArray[self.id] = DFSUtils.count

                        
        return DFS()
                    
                    
        