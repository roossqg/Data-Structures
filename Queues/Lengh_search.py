from collections import deque

class queue_digraph():
    def __init__(self,hash_names,arr=[]):
        self.arr=[]#--> our stack
        self.hash_names=hash_names
        

    def mapping(self,graph=''): #put on the graph tree

        c=input('Is this graph followed by other before?(graph,1 for cancel) :')
        if c == True:
            self.hash_names[f'{c}'].append(graph)

        elif c == 1:
            b=input('There any graph after this graph? (graph/1): ')

            if b == 1:
                self.hash_names[f'{graph}']=[]

            else:
                self.hash_names[f'{graph}']=[graph]





    def search(self,target):
#select your graph start point:

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




            

        