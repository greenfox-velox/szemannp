students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

def get_candies(student_list):
    total = 0
    for student in students:
        if student["candies"] > 4:
            total += 1
    return total

print(get_candies(students))


# def summarize_function(list):
#     sumall = 0
#     for i in range(len(list)):
#         sumall += list[i]
#     return sumall
#
# print(summarize_function(numbers))
