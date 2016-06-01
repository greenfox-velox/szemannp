# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divider():
    try:
        number = int(input('Enter your number to divide 10 with:\n'))
        return 10 / number
    except ZeroDivisionError:
        return 'fail'

print(divider())
