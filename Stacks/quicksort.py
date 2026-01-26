def quicksort(arr):

    if len(arr)<2:
        return arr
    
    pivot=arr[0]
    bigg=[i for i in arr[1:] if i>=pivot]
    loww=[i for i in arr[1:] if i<pivot]

    return quicksort(loww) + [pivot] + quicksort(bigg) #sum list : list


print(quicksort([33,33,33,55,55,6,222,4,222,6,34,90,3,222,1,3,2]))
