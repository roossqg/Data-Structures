import random
target=127#random.randint(0,100)
p=[x for x in range(0,128)] #needs any order for algorithm func
print(p)
print(target)

high=len(p)-1
low=int(0)
d=int((low+high)/2) #calculates for lower, exp 0,100 : 50 (0-99)
#rint(p[int(((low+high)/2))])

def binary_search(p,high,low,target):
    k=0
    while low<=high:
        same=int((high+low)/2)
        teste=p[same]
        if teste==target:
            return same,k
        elif teste>target:
            high=same-1 #first phase: list full
        elif teste<target:
            low=same+1 #second phase : list full
        k+=1
    return None

print(binary_search(p,high,low,target)) #bins= O(log2 n), n=100>> try= 6.644


    