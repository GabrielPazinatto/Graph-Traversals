
class Edge:
    v1 = int()
    v2 = int()
    weight = int()
    
    def __init__(self, v1, v2, w)->None:
        self.v1 = v1
        self.v2 = v2
        self.weight = w
    
    def __string__(self)->str:
        return('[' + str(self.v1) + ", " + str(self.v2) + ", " +str(self.weight) + ']')
        
    def print(self)->None:
        print('[' + str(self.v1) + ", " + str(self.v2) + ", " +str(self.weight) + ']')
        
class Graph:
    vertexes = int()
    adj_list = []
    
    def __init__(self, vertexes, adj_list = None) -> None:
        
        if adj_list == None:
            for i in range(vertexes + 1): self.adj_list.append([])
        else: self.adj_list = adj_list

        self.vertexes = vertexes
        
    def print(self):
        for i in range(len(self.adj_list)):
            for edge in self.adj_list[i]:
                edge.print()
        
    def reset(self) -> None:
        self.__init__()
        
    def cost(self) -> int:
        cost = 0
        for edge in self.adj_list:
            cost = cost + edge.weight
        return cost
    
    def add_edge(self, new_v1 = 0, new_v2 = 0, new_weight = 0) -> None:
        
        v1 = min(new_v1, new_v2)
        v2 = max(new_v1, new_v2)
        
        new_edge = Edge(v1, v2, weight)
        
        if self.adj_list[v1] == []:
            self.adj_list[v1] = [new_edge]
        else: self.adj_list[v1].append(new_edge)
        
        if self.adj_list[v2] == []:
            self.adj_list[v2] = [new_edge]
        else: self.adj_list[v2].append(new_edge)

    def DFS(self, v = 0, visited = None, result = None) -> list:
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
    
v1 = None
v2 = None
weight = None

vertexes = int(input())

graph = Graph(vertexes)
    
while(v1 != 0 or v2 != 0):
    v1, v2= str.split(input("Input an edge: "))
    v1 = int(v1)
    v2 = int(v2)
    #weight = int(weight)
    
    graph.add_edge(v1,v2,weight)
    
graph.print()
        
print(graph.DFS())
