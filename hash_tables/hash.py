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

#print(hash_func(arr))


#case 1:
#phone num list : names
#index = sum of letter codes % hash table size

#You could use diferent patterns of nums for eliminate collisions
letter_code={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10
             ,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19
             ,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':27}

def hash_phone_num(name):

    hash_idx = sum([letter_code[f'{hash}'] for hash in name])


    hash_idx = hash_idx % len(name)
    return f' idx hash of {name}:{hash_idx}'

    #now you can put the phone number of the 'name' in idx hash num
    # of a list and acess it with O(1) Complexity
    

print(hash_phone_num('normie'))


#case 2:
#bacteria num size
# aaaa = size

def bac(aaaa_model):

    aaaa_count=len(aaaa_model)
    return aaaa_count
#you can put each num size on a link list and sort them