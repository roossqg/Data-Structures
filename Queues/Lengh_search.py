class queue():
    def __init__(self,arr,hash_names,target):
        self.arr=[]#--> our stack
        self.hash_names=hash_names
        self.target=target

    def mapping(self):
        #we assume that hash map is sort with names using vector where: key: first stack,item:second stack
        for x in self.hash_names:
            self.arr[-1] = self.hash_names[f'{x}'] # first in - first out
            