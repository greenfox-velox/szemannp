# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    file = open(file_name)
    text = ""
    for line in file:
        sorted_line = line[0: -1: 2]
        text += (sorted_line + "\n")
    file.close()
    return text