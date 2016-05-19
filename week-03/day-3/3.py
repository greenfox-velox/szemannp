# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

class Pirate:
    def __init__(self):
        self.rumAmount = 0
    def drink_rum(self):
        self.rumAmount += 1
        return(self.rumAmount)
    def hows_goin_mate(self):
        if self.rumAmount >= 5:
            return ("Yarrrr!")
        else:
            return ("Nothin")

blackbeard = Pirate()
blackbeard.drink_rum()
blackbeard.drink_rum()
blackbeard.drink_rum()
blackbeard.drink_rum()
blackbeard.drink_rum()
blackbeard.drink_rum()
print(blackbeard.hows_goin_mate())
