
class Edge:
    v1 = int()         # first vertex
    v2 = int()         # second vertex
    weight = int()     # cost from travelling from v1 to v2
    
    def __init__(self, v1, v2, w)->None:
        self.v1 = v1
        self.v2 = v2
        self.weight = w
    
    def __string__(self)->str:
        return('[' + str(self.v1) + ", " + str(self.v2) + ", " +str(self.weight) + ']')
        
    def print(self)->None:
        print('[' + str(self.v1) + ", " + str(self.v2) + ", " +str(self.weight) + ']')
        
class Graph:
    vertexes = int()     # number of vertexes
    adj_list = []        # adjacency list
    directed = False     # tells if the graph is directed or not (WIP)
    
    def __init__(self, vertexes, directed = False, adj_list = None) -> None:
        if adj_list == None:
            for i in range(vertexes + 1): self.adj_list.append([]) #initializes the adjacency list with empty lists
        else: self.adj_list = adj_list

        self.vertexes = vertexes
        self.directed = directed
        
    def print(self):
        print("[v1, v2, weight]")
        for i in range(len(self.adj_list)):
            for edge in self.adj_list[i]:
                edge.print()
        
    def reset(self, vertexes) -> None:
        self.__init__(vertexes)
        
    def cost(self) -> int: # returns the sum of the weight of all the edges
        cost = 0
        for edge in self.adj_list:
            cost = cost + edge.weight
        return cost
    
    def add_edge(self, new_v1 = 0, new_v2 = 0, new_weight = 0) -> None: #adds a new edge ([v1,v2,w]) to the graph
        
        v1 = min(new_v1, new_v2)
        v2 = max(new_v1, new_v2)
        
        new_edge = Edge(v1, v2, weight)
        
        if self.adj_list[v1] == []:
            self.adj_list[v1] = [new_edge]         #if list is empty, it becomes a list with new_edge only
        else: self.adj_list[v1].append(new_edge)   #if list is not empty new_edge is simply appended
        
        if self.adj_list[v2] == []:
            self.adj_list[v2] = [new_edge]
        else: self.adj_list[v2].append(new_edge)

    def DFS(self, v = 0, visited = None, result = None) -> list: #depth first search
        if visited == None: visited = [False]*self.vertexes
        if result == None: result = []
        
        visited[v] = True
        result.append(v)
        
        for edge in self.adj_list[v]:
            if not visited[edge.v1]: 
                self.DFS(edge.v1, visited, result)
            if not visited[edge.v2]:
                self.DFS(edge.v2, visited, result)
                
        return result
    
    def BFS(self, v = 0, visited = None, queue = None, result = None) ->list: #breadth first search
        if visited == None: visited = [False]*self.vertexes
        if result == None: result = []
        if queue == None: queue = []
    
        visited[v] = True
        queue.append(v)
        
        while(queue):
            v = queue.pop(0)
            result.append(v)
            
            for edge in self.adj_list[v]:
                if not visited[edge.v1]:
                    queue.append(edge.v1)
                    visited[edge.v1] = True
                    
                if not visited[edge.v2]:
                    queue.append(edge.v2)
                    visited[edge.v2] = True
        
        return result
    
v1 = None
v2 = None
weight = None

try:
    input_file = open("./test_input.txt")
except:
    exit(1)

line = input_file.readline()

vertexes = int(line)

graph = Graph(vertexes)
    
while(v1 != 0 or v2 != 0):
    v1, v2= str.split(input_file.readline())
    v1 = int(v1)
    v2 = int(v2)
    #weight = int(weight)
    
    graph.add_edge(v1,v2,weight)
    
graph.print()

print("DFS: " + str(graph.DFS()))
print("BFS: " +  str(graph.BFS()))
