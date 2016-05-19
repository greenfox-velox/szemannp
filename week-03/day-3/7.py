# create a function that takes a list and returns a new list with all the elements doubled

source_list =[5, 7, 12, 34, 19, 2, 8]

def get_double():
    for i in range(0, len(source_list)):
        source_list[i] *= 2
    return (source_list)

print(get_double())
