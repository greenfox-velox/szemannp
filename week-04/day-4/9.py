# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def separator(input_string):
    if len(input_string) == 1:
        return input_string[0]
    else:
        return separator(input_string[0:len(input_string) - 1]) + '*' + (input_string[len(input_string) - 1])

print(separator('kugsdfugowugfslcj'))
