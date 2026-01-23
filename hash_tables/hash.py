#no dicts:

def hash_func(obj=0,arr=[]):

    #could be an id class indeed INT
    val=int(input("Enter your hash: "))
    #add
    if arr[val] == False and obj!=0:
        arr[val] = obj
        
    #show
    if obj==0:
        print(arr[val])

    #already on table:
    if arr[val]!= obj:
        print("This hash already exists!")

arr=['apple','orange','rice']

print(hash_func(arr))
