names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list

def short_string_func(input_list):
    for i in range(len(input_list)):
        if len(input_list[i - 1]) > len(input_list[i]):
            minLength = input_list[i]
    print(minLength)

short_string_func(names)
