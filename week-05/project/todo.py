import sys
import csv

class ToDo():

    def __init__(self):
        self.list_file_name = 'todo_list.csv'
        self.complete = '[x]'
        self.incomplete = '[ ]'
        self.default_state = 'False'

    def sort_user_input(self):
        if len(sys.argv) == 1:
            self.get_usage_info()
        if len(sys.argv) >= 2:
            self.handle_user_input()

    def handle_user_input(self):
        if sys.argv[1] == '-l':
            self.print_todo_list()
        elif sys.argv[1] == '-a':
            self.add_new_task()
        elif sys.argv[1] == '-r':
            self.remove_input_handler()
        elif sys.argv[1] == '-c':
            self.mark_task_checked()
        else:
            raise ValueError('Unsupported argument, please try again.')
            self.get_usage_info()

    def get_usage_info(self):
        file_menu = open('usage.txt')
        list_menu = file_menu.read()
        file_menu.close()
        print(list_menu)
        return

    def touch_new_list(self):
        with open(self.list_file_name, 'a') as todo_list_file:
            todo_list_rows = csv.reader(todo_list_file, delimiter=';')
        todo_list_file.close()

    def get_todo_file_length(self):
        num_lines = sum(1 for line in open('todo_list.csv'))
        self.num_lines = num_lines
        return self.num_lines

    def add_new_task(self):
        with open(self.list_file_name, 'a', newline = '') as todo_list_file:
            todo_list_content_add = csv.writer(todo_list_file)
            formatted_input = ('False; ' + sys.argv[2])
            if len(sys.argv) > 2:
                todo_list_content_add.writerow([formatted_input])
            else:
                print('Unable to add, no new task was given')
        todo_list_file.close()
        print('New task successfully added!')
        return

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
        with open(self.list_file_name, 'r') as file_todo:
            todo_list = list(file_todo)
            del todo_list[delete_line - 1]
        with open(self.list_file_name, 'w') as file_todo:
            for n in todo_list:
                file_todo.write(n)
        print('Task successfully removed!')
        print(self.print_todo_list())

    def print_todo_list(self):
        with open(self.list_file_name, 'r') as todo_list_file:
            todo_list_content = csv.reader(todo_list_file, delimiter = ';')
            formatted_list_content = ''
            string_counter = 1
            for line in todo_list_content:
                formatted_list_content += (str(string_counter) + ' - ' + self.get_task_status(line[0]) + ' ' + line[1] + '\n')
                string_counter += 1
        todo_list_file.close()
        print('\n')
        print(formatted_list_content)
        return

    def get_task_status(self, status):
        if status == 'True':
            return self.complete
        return self.incomplete

    def mark_task_checked(self):
        with open(self.list_file_name, 'r') as todo_list_file:
            todo_list_rows = csv.reader(todo_list_file, delimiter=';')
            formatted_list_content = []
            for item in todo_list_rows:
                formatted_list_content.append(item)
            if formatted_list_content[int(sys.argv[2]) - 1][0] == 'False':
                formatted_list_content[int(sys.argv[2]) - 1][0] = 'True'
        todo_list_file.close()
        with open(self.list_file_name, 'w') as todo_list_file:
            for item in formatted_list_content:
                todo_list_file.write(item[0] + ';' + item[1] + '\n')
        todo_list_file.close()
        print(self.print_todo_list())
        print('Task successfully set to completed')
        return

workywork = ToDo()
workywork.sort_user_input()
