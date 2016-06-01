import sys

class ToDo():

    def get_usage_info(self):
        read_menu = open('usage.txt')
        list_menu = read_menu.read()
        read_menu.close()
        return(list_menu)


workywork = ToDo()

# print(workywork.get_usage_info())
