# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    file = open(file_name)
    text = "" 
    for line in file:
        sorted_line = ""
        for chars in range(len(line.rstrip()) -1, -1, -1):
            sorted_line += line.rstrip()[chars]
        text += sorted_line + "\n"  
    file.close()
    return text
