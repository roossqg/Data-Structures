def box_call(first_box):
    print("FIRST BOX")
    print(f"1: {first_box}")



def first(name):
    print(f"hello {name}") #stack -> f|

    box_call(name) # stack --> s|f (second about fist):

    print(f"bye {name}") # stack --> f|

