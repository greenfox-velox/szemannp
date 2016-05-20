def get_palindrome(input):
    result = input
    x = 1
    for i in range(len(input)):
        container = input[-x]
        result += container
        container = None
        x +=1
    return result

print(get_palindrome('safranek'))