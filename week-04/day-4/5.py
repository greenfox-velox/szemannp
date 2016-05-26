# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def get_bunny_ears_number(number_of_bunnies):
    if number_of_bunnies <= 1:
        return 2
    else:
        return 2 + get_bunny_ears_number(number_of_bunnies - 1)

print(get_bunny_ears_number(10))
