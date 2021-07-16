import heapq
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
        sizeRow = len(forest)
        sizeCol = len(forest[0])
        heapArr = []
        
        totalTrees = 0
        if forest[0][0] == 0:
            return -1
        
        for i in range(sizeRow):
            for j in range(sizeCol):
                if forest[i][j] > 1:
                    heapq.heappush(heapArr,(forest[i][j],i,j))
        
        def bfs(src1,src2,dest1,dest2):
            if src1 == dest1 and src2 == dest2:
                return 0
            visited = set()
            count = 0
            queue = [(src1,src2)]
            visited.add((src1,src2))
            queueUtil = []
            while queue:
                count += 1
                while queue:
                    node = queue.pop(0)
                    #print(node)
                    for x,y in [(node[0]+1,node[1]),(node[0]-1,node[1]),(node[0],node[1]+1),(node[0],node[1]-1)]:
                        if x == dest1 and y == dest2:
                            return count
                        if 0<=x<sizeRow and 0<=y<sizeCol and forest[x][y] != 0:
                            if (x,y) not in visited:
                                queueUtil.append((x,y))
                                visited.add((x,y))
                queue = queueUtil[:]
                queueUtil = []
            return -1
        
        
        res = 0
        src1 = src2 = 0
        
        while heapArr:
            val,i,j = heapq.heappop(heapArr)
            dist = bfs(src1,src2,i,j)
            if dist == -1:
                return -1
            res += dist
            src1 = i
            src2 = j
                             
        return res