class Graph:
    def __init__(self,vertices=0):
        self.nodes = {}
        self.vertices = vertices
    
    def addEdge(self,source,destination):
        if source in self.nodes:
            self.nodes[source].append(destination)
        else:
            self.nodes[source] = [destination]
    
    def dfsUtil(self,node,visited):
        if node in visited:
            return
        print(node)
        visited.add(node)
        if node in self.nodes:
            for vertices in self.nodes[node]:
                if vertices not in visited:
                    self.dfsUtil(vertices,visited)
        return
    
    def dfs(self):
        visited = set()
        for node in self.nodes:
            if node not in visited:
                self.dfsUtil(node,visited)
        return
    
    def topologySortUtil(self,node,visited,stack):
        if node in visited:
            return
        #print(node)
        visited.add(node)
        if node in self.nodes:
            for vertices in self.nodes[node]:
                if vertices not in visited:
                    self.topologySortUtil(vertices,visited,stack)
        stack.append(node)
        return    
        
    def topologySort(self):
        visited = set()
        stack = []
        for node in self.nodes:
            if node not in visited:
                self.topologySortUtil(node,visited,stack)
        
        return stack
    
    def cycleUtil(self,node,visited,stack):
        if node not in self.nodes:
            return True
        if node in visited:
            return True
        if node in stack:
            return False
        
        stack.add(node)
        for vertice in self.nodes[node]:
            if self.cycleUtil(vertice,visited,stack) == False:
                return False
        visited.add(node)
        return True
    
    def isCycle(self):
        visited = set()
        for node in self.nodes:
            stack = set()
            if self.cycleUtil(node,visited,stack) == False:
                return False
        return True
            
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graphObj = Graph(numCourses)
        
        for vertices_ in prerequisites:
            graphObj.addEdge(vertices_[0],vertices_[1])
        
        #print(graphObj.nodes)
        #visited = set()
        #graphObj.dfs()
        #print(graphObj.topologySort())
        return graphObj.isCycle()