class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """"m = len(mat)
        n = len(mat[0])
        
        ans = [[0 for i in range(n)] for j in range(m)]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        visited = set()
        
        def bfs(queue):
            distance = 0
            queueUtils = []
            while queue:
                temp = queue.pop(0)
                for a, b in dirs:
                    if -1 < a + temp[0] < m and -1 < b + temp[1] < n:
                        if (temp[0]+a, temp[1]+b) in visited:
                            distance += 1
                            return distance
                        elif mat[temp[0]+a][temp[1]+b] == 0:
                            distance += 1
                            return distance
                        else:
                            queueUtils.append((temp[0]+a, temp[1]+b))
                if len(queue) == 0:
                    distance += 1
                    queue = queueUtils[:]
                    queueUtils = []
            return distance
        
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    queue = []
                    queue.append((i, j))
                    distance = bfs(queue)
                    ans[i][j] = distance
                else:
                    visited.add((i, j))
        
        return ans"""
        n,m = len(mat), len(mat[0])
        
        ans = [[-1 if mat[i][j]!=0 else 0 for j in range(m)] for i in range(n)]
        dirxn = [(1,0),(-1,0),
                (0,1),(0,-1)]
        
        stack = collections.deque()
        seen = set()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    seen.add((i,j))
                    stack.append((i,j,0))
        
        while stack:
            i,j,depth = stack.popleft()
            ans[i][j] = depth
            for dx, dy in dirxn:
                x,y = i+dx, j+dy
                if 0<=x<n and 0<=y<m and (x,y) not in seen:
                    seen.add((x,y))
                    stack.append((x,y,depth+1))
        return ans
    