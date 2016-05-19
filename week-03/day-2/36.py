# write a function that reverses a list

my_list = [3, 4, 5, 6, 7]

# def list_reverse(input_list):
#     input_list.reverse()
#     return input_list
#
# print(list_reverse(my_list))

def revert(input):
    reverse = []
    for i in range(len(input)-1, -1, -1):
        reverse += [input[i]]
    return reverse

print(revert(my_list))
