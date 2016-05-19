# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack:

    def __init__(self):
        self.size = 0
        self.stack_of_elements = [2, 4, 7, 10, 12]
    def get_size(self):
        self.size = len(self.stack_of_elements)
        return self.size
    def stack_push(self, add_element):
        self.add_element = add_element
        self.stack_of_elements.append(self.add_element)
        return self.stack_of_elements
    def stack_pop(self):
        self.stack_of_elements.pop()
        return self.stack_of_elements

haystack = Stack()

print(haystack.get_size())
print(haystack.stack_push(5))
print(haystack.stack_pop())
