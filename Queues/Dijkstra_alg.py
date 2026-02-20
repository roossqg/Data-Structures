#g1 -w- g2 -w- g3 -w- g1

#let's use graph tree as an concept:

from Queues.Graph_tree import Graph_Tree

class Dijkstra(Graph_Tree): #now,hash names has graphs as dicts where his values are their edges weights
    def __init__(self, hash_names,hash_edges):
        super().__init__(hash_names)
        self.hash_edges=hash_edges


    def put_graph(self, graph=''):
        base_floor = input('Is this graph followed by other before?(node/exit) :')

        if base_floor != 'exit' :
            edge_weight = int('Edge: ')
            self.hash_edges[f'{base_floor}'][f'{graph}'] = edge_weight
            self.hash_names[f'{base_floor}'].append(graph)

        elif base_floor == 'exit' :
            #graph link below
            self.hash_edges[f'{graph}']={}
            self.hash_names[f'{graph}']=[]
            
            while True :
                b=input('There any graph after this graph? (node/not): ')
                
                if b == 'not':
                    break

                else:
                    edge_weight = int('Edge: ')
                    self.hash_names[f'{graph}'][f'{b}'] = edge_weight
                    self.hash_names[f'{graph}'].append(b)

        return self.hash_names
    
    def minimum_cost(self,start):
        destiny = float('inf')
        minimum_cost_edge=None

        for graph in start:
            cost = start[graph]

            if cost < minimum_cost_edge:
                minimum_cost_edge = cost
                minimum_edge = graph

        return minimum_cost_edge


    
    def search(self, target):
        processesd_graphs = []
        minimum_way = {}

        #start:
        point=input('Select the graph as reference: ')
        start_graph = self.hash_names[f'{point}'] # -> list of graph to costs

        based_way_costs = self.hash_edges[start_graph]

        node = self.minimum_cost(based_way_costs)
        while node is not None:

            cost = based_way_costs[node] # less cost after start
            neighs = self.hash_names[node]

            for node_graphs in neighs.keys() # ->> next edges after this graph
            #process each neigh cost

                actual_cost = cost + neighs[node_graphs] # hash_edges[node][neigh_graph n]
                if  based_way_costs[node_graphs] > actual_cost: # start node to neigh node a > neigh node a + new way to
                    based_way_costs[node_graphs] = actual_cost
                    minimum_way[f'{node_graphs}'] = node

            #next edge from node 

            processesd_graphs.append(node)
            node = self.minimum_cost()
