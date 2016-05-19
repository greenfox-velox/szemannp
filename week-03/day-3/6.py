# create a function that takes a list and returns a new list that is reversed
source_list =[5, 7, 12, 34, 19, 2, 8]

def get_reverse(input_list):
    input_list.reverse()
    return input_list

print(get_reverse(source_list))
