# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person():
    name = str(input('Enter your name:\n'))
    birthdate = int(input('Enter your year of birth:\n'))
    if birthdate < 0 or birthdate > 2016:
        raise ValueError('Very invalid year of birth!')

pista = Person()

print(pista.name, pista.birthdate)
