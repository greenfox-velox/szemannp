def get_palindrome(input):
    result = input
    x = 1
    for i in range(len(input)):
        container = input[-x]
        result += container
        x +=1
        container = None
    return result

print(get_palindrome('safranek'))