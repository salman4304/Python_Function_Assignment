# Write a function to flatten a nested list.
def flatten_list(nested_list):
    flat_list=[]
    for sublist in nested_list:
        # isinstance function returns true or false checks whether specified item data type matches with mentioned data type 
        if isinstance(sublist,list): 
           flat_list.extend(sublist)
        else:
            flat_list.append(sublist)
    return flat_list

nested=[1,[2,3],[4,5],[6,7]]
print(flatten_list(nested))