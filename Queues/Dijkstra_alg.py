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

        for vector in range(self.size):
            vector = None
            minimum_distance = float('inf')

            for sub_vector in range(self.size):
                if distances[sub_vector] < minimum_distance and not graphs_visited[sub_vector]:
                    minimum_distance = distances[sub_vector]
                    vector = sub_vector

                if vector is None:
                    break

                graphs_visited[sub_vector] = True


            for vector_edge in range(self.size):
                if self.graph_matrix[vector][vector_edge] != 0 and not graphs_visited[vector_edge]:
                    new_cost = distances[vector] + self.graph_matrix[vector][vector_edge]
                    if new_cost < distances[vector_edge]:
                        distances[vector_edge] = new_cost

                        
        return distances




