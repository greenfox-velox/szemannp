import sys

class ToDo():

    def sort_user_input(self):
        if len(sys.argv) == 1:
            self.get_usage_info()
        if len(sys.argv) >= 2:
            self.handle_user_input()

    def handle_user_input(self):
        if sys.argv[1] == '-l':
            self.get_todo_list()
        elif sys.argv[1] == '-a':
            self.add_new_task()
        elif sys.argv[1] == '-r':
            self.remove_input_handler()
        elif sys.argv[1] == '-c':
            pass
            print('# undone: set_task_completed()')
        else:
            raise ValueError('Unsupported argument, please try again.')
            self.get_usage_info()

    def get_usage_info(self):
        file_menu = open('usage.txt')
        list_menu = file_menu.read()
        file_menu.close()
        print(list_menu)
        return

    def get_todo_list(self):
        try:
            file_todo = open('todo_list.txt')
            todo_list = file_todo.readlines()
            print('\n')
            if len(todo_list) > 0:
                for line in range(len(todo_list)):
                    print(line + 1, ' - ', todo_list[line].rstrip())
            else:
                return 'There is nothing to do today!'
            file_todo.close()
            return ''
        except FileNotFoundError:
            touch_new_list()

    def touch_new_list(self):
        file_todo = open('todo_list.txt', 'a')
        file_todo.close()
        return

    def add_new_task(self):
        file_todo = open('todo_list.txt', 'a')
        if len(sys.argv) > 2:
            file_todo.write(sys.argv[2])
            file_todo.close()
        else:
            print('Unable to add, no new task was given')
        print('New task successfully added')
        print(self.get_todo_list())
        return

    def get_todo_file_length(self):
        num_lines = sum(1 for line in open('todo_list.txt'))
        self.num_lines = num_lines
        return self.num_lines

    def remove_input_handler(self):
        line_index_to_remove = 0
        num_lines = self.get_todo_file_length()
        if len(sys.argv) > 2:
            line_index_to_remove = int(sys.argv[2])
            if line_index_to_remove <= num_lines:
                self.remove_task()
            else:
                raise ValueError('Unable to remove: item index is out of range.')
        else:
            print('Unable to remove: index not present. Try again.')
        return

    def remove_task(self):
        delete_line = int(sys.argv[2])
        with open("todo_list.txt","r") as file_todo:
            todo_list = list(file_todo)
            del todo_list[delete_line - 1]
        with open("todo_list.txt","w") as file_todo:
            for n in todo_list:
                file_todo.write(n)
        print('Task successfully removed!')
        print(self.get_todo_list())
        return


workywork = ToDo()
workywork.sort_user_input()
