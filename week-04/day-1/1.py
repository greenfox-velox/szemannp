# 1. Create a method that reads all contents of a file when its name given as param
def readfile(file_name):
    rf = open(file_name)
    content = rf.read()
    rf.close()
    return content

# 2. Create a method that gets a file_name and a number as param and reads the numberth line of the file
def readline(file_name, number):
    rl = open(file_name)
    for i in range(number):
        result = rl.readline()
    rl.close()
    return result.rstrip()

# 3. Create a method that gets a long sentence as param and gives back the contained words in a list
def words(sentence):
    sentence = sentence.strip('.')
    word_count = sentence.split()
    return word_count

# 4. Create a method that gets a list of words and creates a sentence with the words separated by spaces
def sentence(words):
    sentence = " ".join(words) + "."
    return sentence

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    char_list = []
    code_list = []
    for i in string:
        char_list += i
    for i in range(0, len(char_list)):
        code_list.append(ord(char_list[i]))
    return code_list

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(char_codes):
    string = ""
    for i in char_codes:
        string += chr(i)
    print(string)
    return string


