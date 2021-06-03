class Graph:
    def __init__(self,vertices=0):
        self.nodes = {}
        self.vertices = vertices
    
    def addEdge(self,src,dest):
        if src not in self.nodes:
            self.nodes[src] = [dest]
        else:
            self.nodes[src].append(dest)
    
    def cycleUtil(self,node,visited,recurSet):
        if node not in self.nodes:
            return True
        if node in visited:
            return True
        if node in recurSet:
            return False
        
        recurSet.add(node)
        for vertex in self.nodes[node]:
            if self.cycleUtil(vertex,visited,recurSet) == False:
                return False
        visited.add(node)
        return True
    
    def isCycle(self):
        visited = set()
        for node in self.nodes:
            recurSet = set()
            if self.cycleUtil(node,visited,recurSet) == False:
                return True
        return False
    
    def topologyUtil(self,node,visited,stack):
        if node in visited:
            return
        visited.add(node)
        if node in self.nodes:
            for vertex in self.nodes[node]:
                if vertex not in visited:
                    self.topologyUtil(vertex,visited,stack)
        stack.append(node)
        return
    
    def topologySort(self):
        visited = set()
        stack = []
        for node in self.nodes:
            if node not in visited:
                self.topologyUtil(node,visited,stack)
        #print(stack)
        if stack:
            return stack
        return stack
            
            
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graphObj = Graph(numCourses)
        
        for val in prerequisites:
            graphObj.addEdge(val[0],val[1])
        for i in range(numCourses):
            if i not in graphObj.nodes:
                graphObj.nodes[i] = []
        if graphObj.isCycle():
            return []
        
        return graphObj.topologySort()
            
            
            
            
        