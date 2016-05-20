# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet_person(self):
        return "Greetings, " +self.first_name +self.last_name

class Student:
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.grade_list = []
        self.avarage = None
        Person.__init__(self)
    def add_grade(self, grade):
        self.grade = grade
        if self.grade < 1:
            return("Invalid value!")
        elif self.grade > 5:
            return("Invalid value!")
        else:
            self.grade_list.append(self.grade)
            return self.grade_list

    def salute(self):
        super(Student, self).greet_person()
        # self.avarage = sum(self.grade_list) / len(self.grade_list)
        # return self.avarage

# class Student(Person):
#     def __init__(Person):
#         pass
#     def add_grade(self, grade):
#         self.grade = grade
#         if self.grade < 1:
#             return("Invalid value!")
#         elif self.grade > 5:
#             return("Invalid value!")
#         else:
#             self.grade_list.append(self.grade)
#             return self.grade_list

    # def salute(self):
    #     self.avarage = sum(self.grade_list) / len(self.grade_list)
    #     return "Greetings, " +self.first_name, +self.last_name ", my avarage is" +self.avarage

majom = Person('Saf ', 'Ranek')
csimpi = Student
print(majom.greet_person())
# print(csimpi.add_grade(5))
# print(csimpi.add_grade(4))
# print(csimpi.add_grade(1))
print(csimpi.salute)
