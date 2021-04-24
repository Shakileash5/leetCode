class Graph:
    def __init__(self,vertises):
        self.vertices = vertises
        self.graphNodes = {}
    
    def addEdge(self,src,dst):
        keys = self.graphNodes.keys()
        if src not in keys:
            self.graphNodes[src] = [dst]
        else:
            self.graphNodes[src].append(dst)
        keys = self.graphNodes.keys()
        if dst not in keys:
            self.graphNodes[dst] = [src]
        else:
            self.graphNodes[dst].append(src)
    
    def bfs(self,root):
        visited = [False]*self.vertices
        
        visited[root] = True
        queue = [root]
        queue2 = []
        height = 1
        
        while(queue):
            rootNode = queue.pop(0)
            #print(queue)
            for i in self.graphNodes[rootNode]:
                if visited[i] == False:
                    queue2.append(i)
                    visited[i] = True
            if queue == []:
                queue = queue2[:]
                queue2 = []
                if(queue):
                    height+=1
        return height

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graphObj = Graph(n)
        if edges == []:
            return [0]
        sizeR = len(edges)
        for i in graphObj.graphNodes.keys():
            graphObj.graphNodes[i] = list(set(graphObj.graphNodes[i]))
        sizeC = len(edges[0])
        minSet = [1000,[]]
        for i in range(sizeR):
            for j in range(1,sizeC):
                graphObj.addEdge(edges[i][0],edges[i][j])
        
        #print(graphObj.graphNodes)
        """
        for i in range(n):
            height = graphObj.bfs(i)
            #print(height,i)
            if minSet[0]>height:
                minSet[0] = height
                minSet[1] = [i]
            elif minSet[0] == height:
                minSet[1].append(i)"""
        
        graph = graphObj.graphNodes
        q = []
        for node in graph:
            if len(graph[node]) == 1 or len(graph[node]) == 0:
                q.append(node)
        #print(q)
        visited = set()
        while n - len(visited) > 2:
            cur_size = len(q)
            while cur_size > 0:
                node = q.pop(0)
                visited.add(node)
                for nei in graph[node]:
                    graph[nei].remove(node)
                    if len(graph[nei]) == 1:
                        q.append(nei)
                del graph[node]
                cur_size -= 1
        
        return q
            