# 6. We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or
# multiplication).

def get_bunny_ears_in_line(bunnies_in_line):
    if bunnies_in_line <= 2:
        return 5
    else:
        return 5 + get_bunny_ears_in_line(bunnies_in_line - 2)

print(get_bunny_ears_in_line(10))
