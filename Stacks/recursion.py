
#[2,3,8,9] -> [3,8,9] -> [8,9]
def sum_arr(arr):
    #base: 1 element
    #base 2: 0 elements
     #x will change in every recursion
    if len(arr)==1:
        return arr[-1]
    else:
        return arr[0]+sum_arr(arr=arr[0+1:])
    
#--> basically each func will put on a stack and execute partially yet the base case,where returns and remove funcs from stacks

def search_list(arr):
    #base count: []=1 elements:stop+1)last
    if len(arr)>1:
        return 1+search_list(arr=arr[0+1:]) #change last array in each func on stack



exp1=[2,5,6,2,5.3]
t=search_list(exp1)
print(t)

def search(box):
    for item in box:
        if item.is_box():  #--> is a function
            if item.is_a_black_box():
                pass
            else:
                search(item) # recursion the box object
        elif item.is_key():
            return "Key discovered!"
