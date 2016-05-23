# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    file = open(file_name)
    sorted_file = ""
    for line in reversed(file.readlines()):
        ordered_line = ""
        for i in range(0, len(line.rstrip())):
            ordered_line += line.rstrip()[i]
        sorted_file += ordered_line + "\n"
    file.close()
    return sorted_file