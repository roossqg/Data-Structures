#g1 -w- g2 -w- g3 -w- g1

#let's use graph tree as an concept:

class Dijkstra():
    def __init__(self,size):
        self.graph_matrix = [[0] * size for g in range(size)] # -> each graph routes (one to many)
        self.size = size
        self.graphs_vertex = [''] * size # -> each graph
        
    def add_edge (self,v1,v2,weight):
        if 0 <= v1 <= self.size and 0 <= v2 <= self.size :
            self.graph_matrix[v1][v2] = weight
            self.graph_matrix[v2][v1] = weight

    def add_vertex (self,vertex,data): #graph name or dict
        if 0 <= vertex <= self.size:
            self.graphs_vertex[vertex] = data # can modify too

    def dijkstra(self,start_vertex):
        start = self.graphs_vertex[start_vertex]
        distances = [float('inf')] * self.size
        distances[start] = 0
        graphs_visited = [False] * self.size




