# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def get_amount_of_lines(file_name):
    try:
        num_lines = sum(1 for line in open(file_name))
        return num_lines
    except FileNotFoundError:
        return '0'
    file_name.close()
print(get_amount_of_lines('linecont.txt'))
