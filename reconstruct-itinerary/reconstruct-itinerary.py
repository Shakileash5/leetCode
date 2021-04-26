class Graph:
    def __init__(self):
        self.graphNodes = {}
        self.stack = []
        self.topo = []
    def addEdge(self,src,dst):
        keys = self.graphNodes.keys()
        if src not in keys:
            self.graphNodes[src] = [dst]
        else:
            self.graphNodes[src].append(dst)
            self.graphNodes[src].sort()
        return
    
    def dfsUtil(self,node,visited):
        
        #print(node,visited)
        self.stack.append(node)
        if node in self.graphNodes.keys():
            for i,neighbour in enumerate(self.graphNodes[node]):
                if (node,i,neighbour) not in visited:
                    visited.add((node,i,neighbour))
                    self.dfsUtil(neighbour,visited)
        self.topo.append(node)
        
    def dfs(self):
        
        visited = set()
        keys = self.graphNodes.keys()
        if "JFK" in keys:
            #self.stack = ["JFK"]
            self.dfsUtil("JFK",visited)
            #for i in self.graphNodes.keys():
            #    self.dfsUtil(self.graphNodes[i][0],i,visited)
        else:
            keys.sort()
            self.stack = [self.graphNodes[keys[0]]]
            self.dfsUtil(self.graphNodes[keys[0]][0],self.graphNodes[keys[0]],visited)
        #print(self.topo)
        return


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graphObj = Graph()
        
        for nodes in tickets:
            graphObj.addEdge(nodes[0],nodes[1])
        
        #print(graphObj.graphNodes)
        graphObj.dfs()
        
        return graphObj.topo[::-1]