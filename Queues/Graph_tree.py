from collections import deque

class Graph_Tree():
    def __init__(self,hash_names):
        self.hash_names=hash_names
        

    def put_graph(self,graph=''): 
        """
        function for put a graph on a tree
        
        graph: node which you want put on tree
        
        """

        #graph link above 
        base_floor = input('Is this graph followed by other before?(node/exit) :')

        if base_floor != 'exit' :
            self.hash_names[f'{base_floor}'].append(graph)

        elif base_floor == 'exit' :
            #graph link below
            while True :
                b=input('There any graph after this graph? (node/not): ')

                if b != 'not':
                    self.hash_names[f'{graph}']=[]
                    break

                else:
                    self.hash_names[f'{graph}'] += [b]

        return self.hash_names


    def search(self,target):
        """
        here you use a BFS with the Graph Tree to search for a especific information
        
        :param target: model,value,lambda function or others that represents the query result

        """

        point=input('Select the graph as reference: ')

        queue=deque()
        queue += self.hash_names[f'{point}']

        visited=[]
        while queue: #while in queue
            graph=queue.popleft()    #first in-first out

            if not graph in visited:
                if graph == target:
                    return True
        
                else:
                    queue += self.hash_names[f'{graph}']
                    visited.append(graph)

        return 'targed not found'

hash_houses={'house1':['bedroom1'],'house2':['bathroom2','room2']}

test1=Graph_Tree(hash_houses)






            

        