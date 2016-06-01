import sys

class ToDo():

    def get_usage_info(self):
        file_menu = open('usage.txt')
        list_menu = file_menu.read()
        file_menu.close()
        return(list_menu)

    def get_todo_list(self):
        file_todo = open('todo_list.txt')
        todo_list = file_todo.readlines()
        print('\n')
        for line in range(len(todo_list)):
            print(line + 1, todo_list[line].rstrip())
        file_todo.close()
        return ''


workywork = ToDo()

print(workywork.get_usage_info())
print(workywork.get_todo_list())
