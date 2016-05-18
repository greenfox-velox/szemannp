numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function
def summarize_function(list):
    sumall = 0
    for i in range(len(list)):
        sumall += list[i]
    return sumall

print(summarize_function(numbers))
