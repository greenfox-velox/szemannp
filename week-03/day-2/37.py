numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def sort_list_funct(input_list):
    newList = []
    for i in range(len(input_list)):
        if input_list[i] % 2 != 0:
            i += 1
        else:
            newList.append(input_list[i])
            i += 1
    return newList

print(sort_list_funct(numbers))
