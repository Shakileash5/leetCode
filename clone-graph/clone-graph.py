"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class GraphNode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Solution:
    def cloneGraphTwo(self,node):
        
        hashMap = {}
        graph = Node(node.val)
        hashMap[node.val] = graph
        sourceSet = set()
        queue = []
        qeueUtil = []
        visited = set()
        visited.add(node.val)
        queue.append(node)
        def addEdge(graph,neighbor):
            """list_ = [neighbor]
            list_ = graph.neighbors + list_
            graph.neighbors = list_
            """
            graph.neighbors.append(neighbor)
            
        while queue:
            graphNode = queue.pop(0)
            #print(graphNode.val)
            for neighbour in graphNode.neighbors:
                if neighbour.val not in visited:
                    queue.append(neighbour)
                    node_ = Node(neighbour.val)
                    hashMap[neighbour.val] = node_
                    visited.add(neighbour.val)
                if (graphNode.val,neighbour.val) not in sourceSet:
                    #print(sourceSet)
                    sourceSet.add((graphNode.val,neighbour.val))
                    addEdge(hashMap[graphNode.val],hashMap[neighbour.val])            
        
        return graph
        
        
        
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node == None:
            return None
        
        def addEdge(graph,neighbor):
            node = [neighbor]
            node = graph.neighbors+node
            #node.next = graph.neighbors
            graph.neighbors = node
            
            #node = graphNode(source)
            #node.next = graph[destination].neighbors
            #graph[destination].neighbors = node
            
            return
        
        #print(node.val,node.neighbors)
        """graph = Node(node.val)
        
        cloneHash = {}
        visitedSet = set()
        queue = []
        queue.append(node)
        visitedSet.add(node.val)
        sourceSet = set()
        cloneHash[node.val] = graph
        
        while(len(queue)>0):
            tempNode = queue.pop(0)
            #print(tempNode.val)
            for neighbor in tempNode.neighbors:
                #print("source-",tempNode.val,"neighbour-",neighbor.val)
                #graph = Node(tempNode.val)
                #addEdge(graph,tempNode.val,neighbor.val)
                if neighbor.val not in visitedSet:
                    queue.append(neighbor)
                    #print("source-",tempNode.val,"neighbour-",neighbor.val)
                    visitedSet.add(neighbor.val)
                    cloneNeighbor = Node(neighbor.val)
                    cloneHash[neighbor.val] = cloneNeighbor
                    #cloneQueue.append(cloneNeighbor)
                if (tempNode.val,neighbor.val) not in sourceSet:
                    sourceSet.add((tempNode.val,neighbor.val)) 
                    addEdge(cloneHash[tempNode.val],cloneHash[neighbor.val])
                #print((tempNode.val,neighbor.val),sourceSet)
        """
        
        #return graph
        
        return self.cloneGraphTwo(node)