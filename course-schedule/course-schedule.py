class Graph:
    
    def __init__(self,vertices=0):
        '''
            This is an constructor to initialize data members
        '''
        
        self.nodes = {}
        self.vertices = vertices
    
    def addEdge(self,src,dest):
        '''
            This function add nodes to the graph
        '''
        if src not in self.nodes:
            self.nodes[src] = [dest]
        else:
            self.nodes[src].append(dest)
    
    def isCycleUtil(self,node,stack,visited):
        '''
            This is an helper function to check wheather cycle exists in nodes
        '''
        if node not in self.nodes:
            return False
        if node in visited:
            return False
        if node in stack:
            return True
        
        stack.add(node)
        for neighbour in self.nodes[node]:
            if self.isCycleUtil(neighbour,stack,visited):
                return True
        visited.add(node)
        return False
    
    def isCycle(self):
        '''
            This funtion finds wheather cycle exists in nodes
        '''
        visited = set() # to keep track of visited nodes
        for key in self.nodes:
            if key not in visited:
                stack = set()
                if self.isCycleUtil(key,stack,visited):
                    return True
        return False
    
    def dfs(self,node,visited):
        if node not in self.nodes:
            return False
        visited.add(node)
        for key in self.nodes[node]:
            if key not in visited:
                if not self.dfs(key,visited):
                    return False
                if key == node:
                    return True
        return True
            
    def is_cycle(self):
        visited = set() # to keep track of visited nodes
        for key in self.nodes.keys():
            if key not in visited:
                if not self.dfs(key,visited):
                    return False
        return True
    
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graphObj = Graph(numCourses)
        
        for edges in prerequisites:
            graphObj.addEdge(edges[0],edges[1])
        
        return graphObj.isCycle() == False
        
        
        
        