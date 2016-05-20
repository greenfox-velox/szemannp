# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['dad', 'dood', 'eve']

def search_pals(input_str):
    palindrome_list = []
    slice_start = 1
    slice_end = slice_start + 2
    
    for slice_start in range(slice_start, len(input_str)):
        sub_start = input_str[slice_start]
        
        for slice_end in range(slice_end, len(input_str)):
            sub_end = input_str[slice_end]
            
            if input_str[slice_start: slice_end] == input_str[slice_end: slice_start: -1]:
                palindrome_list.append(input_str[slice_start + 1: slice_end])

    return palindrome_list

print(search_pals('dog goat dad duck doodle never'))

# input_str_sub == rev_input_sub  !!!!!!!!!!!