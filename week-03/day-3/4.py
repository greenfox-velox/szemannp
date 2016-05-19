# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student:
    def __init__(self):
        self.grade_list = []
        self.avarage = None
    def add_grade(self, grade):
        self.grade = grade
        if self.grade < 1:
            return("Invalid value!")
        elif self.grade > 5:
            return("Invalid value!")
        else:
            self.grade_list.append(self.grade)
            return self.grade_list

    def get_avarage(self):
        self.avarage = sum(self.grade_list) / len(self.grade_list)
        return self.avarage

majom = Student()

print(majom.add_grade(3))
print(majom.add_grade(2))
print(majom.add_grade(4))
print(majom.add_grade(5))
print(majom.get_avarage())
