# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def remove_x_from_string(input_string):
    if len(input_string) == 0:
        return ''
    elif input_string[len(input_string) - 1] == 'x':
        return remove_x_from_string(input_string[0:len(input_string) - 1])
    else:
        return remove_x_from_string(input_string[0:len(input_string) - 1]) + (input_string[len(input_string) - 1])

print(remove_x_from_string('xljbekhfdxxblsjdxljfxxxRFEG'))
print(input_string)
