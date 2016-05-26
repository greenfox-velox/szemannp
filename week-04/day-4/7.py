# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def get_lowercase_string(input_string):
    if len(input_string) == 0:
        return ''
    elif input_string[len(input_string) - 1] == 'x':
        return get_lowercase_string(input_string[0:len(input_string) - 1]) + 'y'
    else:
        return get_lowercase_string(input_string[0:len(input_string) - 1]) + (input_string[len(input_string) - 1])

print(get_lowercase_string('efxhaXlhexx'))
