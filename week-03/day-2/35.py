# create a function that returns it's input factorial
test = 5

def factorial_function(input):
    value = 1
    for i in range(1, input + 1):
        value = value * i
    return value

print(factorial_function(test))
