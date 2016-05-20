def get_palindrome(input):
    x = 1
    result = input
    for i in range(len(input)):
        palindrome = input[-x]
        result += palindrome
        palindrome = None
        x +=1
    return result

print(get_palindrome('safranek'))