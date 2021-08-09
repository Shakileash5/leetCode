class Graph:
    
    def __init__(self,vertices=0):
        '''
            This is an contructor , to initialize graph objects.
        '''
        self.nodes = {}
        self.vertices = vertices
    
    def addEdge(self,src,dest):
        '''
            This function adds edge to the graph.
        '''
        if src not in self.nodes:
            self.nodes[src] = [dest]
        else:
            self.nodes[src].append(dest)
        
        return
    
    def isCycleUtil(self,node,visited,stack):
        '''
            This function is an utility function of isCycle.
        '''
        
        if node not in self.nodes:
            return False
        if node in visited:
            return False
        if node in stack:
            return True
        
        stack.add(node)
        for neighbour in self.nodes[node]:
            if self.isCycleUtil(neighbour,visited,stack):
                return True
        
        visited.add(node)
        return False
    
    def isCycle(self):
        '''
            This function checks wheather the graph has cycle or not
        '''
        
        visited = set()
        
        for key in self.nodes:
            if key not in visited:
                stack = set()
                if self.isCycleUtil(key,visited,stack):
                    return True
        
        return False
    
    
    def toposortUtil(self,node,visited,stack):
        
        visited.add(node)
        if node in self.nodes:
            for neighbour in self.nodes[node]:
                if neighbour not in visited:
                    self.toposortUtil(neighbour,visited,stack)
        
        stack.append(node)
        return
    
    def toposort(self):
        '''
            This function performs topological sort on the graph.
        '''
        visited = set()
        stack = []
        
        for key in self.nodes:
            if key not in visited:
                self.toposortUtil(key,visited,stack)
        
        #print(stack)
        return stack

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graphObj = Graph(numCourses)
        res = []
        
        for edge in prerequisites:
            graphObj.addEdge(edge[0],edge[1])
        
        
        if graphObj.isCycle():
            return res 
        for i in range(numCourses):
            if i not in graphObj.nodes:
                graphObj.nodes[i] = []
        res = graphObj.toposort()
        return res
        
        
        