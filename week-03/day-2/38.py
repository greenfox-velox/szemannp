numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)

def own_min_list(input_list):
    for i in range(len(input_list)):
        if input_list[i - 1] > input_list[i]:
            minItem = input_list[i]
    print(minItem)

own_min_list(numbers)
