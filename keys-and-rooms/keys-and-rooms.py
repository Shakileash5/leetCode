class Graph:
    def __init__(self,vertices=0):
        self.nodes = {}
        self.vertices = vertices
    
    def addEdge(self,src,dest):
        if src not in self.nodes:
            self.nodes[src] = [dest]
        else:
            self.nodes[src].append(dest)
    
    def dfs(self,node,visited,count):
        visited[node] = True
        count[0] += 1
        
        if node in self.nodes:
            for key in self.nodes[node]:
                if visited[key] == False:
                    self.dfs(key,visited,count)
        return

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        size = len(rooms)
        graphObj = Graph(size)
        
        for i in range(size):
            for key in rooms[i]:
                graphObj.addEdge(i,key)
        
        count = [0]
        visited = [False for i in range(size)]
        graphObj.dfs(0,visited,count)
        
        if count[0] == size:
            return True
        return False
                
                