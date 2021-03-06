from tkinter import *
from random import randint

main = Tk()

canvas = Canvas(main, width = 720, height = 800)
board_size = 10

level_1_board = [[2, 2, 2, 0, 2, 0, 2, 0, 0, 3],
                [2, 0, 0, 0, 2, 0, 2, 0, 0, 2],
                [2, 2, 2, 2, 3, 0, 2, 2, 2, 2],
                [0, 0, 0, 0, 2, 0, 0, 0, 0, 2],
                [2, 0, 3, 0, 2, 2, 2, 3, 0, 2],
                [2, 0, 2, 0, 2, 0, 0, 2, 0, 2],
                [2, 2, 2, 2, 2, 0, 0, 2, 0, 2],
                [2, 0, 0, 0, 2, 2, 2, 2, 0, 2],
                [5, 2, 2, 0, 2, 0, 0, 2, 0, 2],
                [2, 0, 2, 0, 2, 0, 2, 2, 2, 3]]


class ScreenPrinter(object):

    def __init__(self):
        self.playfield = PlayField(level_1_board)
        self.hero = Hero(0, 0)
        self.playfield.set_playfield()

    def print_hero_stats(self):
        self.playfield.create_text(0, 750, text = self.hero)

    def print_playfield(self):
        self.print_tiles()
        self.print_enemies()
        self.print_bosses()

    def print_tiles(self):
        for tile in self.tile_objects:
            tile.draw()

    def print_enemies(self):
        for enemy in self.enemy_objects:
            enemy.draw()

    def print_bosses(self):
        for boss in self.boss_objects:
            boss.draw()

class Stats(object):
    # parentheses in the formulas are used for readability purposes
    def __init__(self, hitpoint = 1, defense_point = 1, strike_point = 1, level = 1):
        self.hitpoint = hitpoint
        self.defense_point = defense_point
        self.strike_point = strike_point
        self.level = level

    def set_hero_stats(self):
        self.hitpoint = 20 + randint(1, 7) + randint(1, 7) + randint(1, 7)
        self.defense_point = randint(1, 7) + randint(1, 7)
        self.strike_point = 5 + randint(1, 7) + randint(1, 7)
        self.level = 1

    # def set_trashmob_stats(self):
    #     self.hitpoint = self.level * 2 * randint(1, 7)
    #     self.defense_point = (self.level // 2) * randint(1, 7)
    #     self.strike_point = self.level * randint(1, 7)
    #
    # def set_boss_stats(self):
    #     self.hitpoint = self.level * 2 * randint(1, 7) + randint(1, 7)
    #     self.defense_point = (self.level // 2) * randint(1, 7) + randint(1, 7) // 2
    #     self.strike_point = self.level * randint(1, 7) + self.level

    def print_stats(self):
        canvas.create_text(board_size * 72 // 2, board_size * 72 + 50, text = self.stat_text)
        print(self.stat_text)

    def get_stats(self):
        self.stat_text = ('Hero:', '(Level: ' + str(self.level) + ') ' + 'HP: ' + str(self.hitpoint) + ' | ' + 'DP: ' + str(self.defense_point) + ' | ' + 'SP: ' + str(self.strike_point))
        return self.stat_text

class Validator(object):

    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    def validate_move_left(self):
        if level_1_board[self.horizontal][self.vertical - 1] >= 2 and self.vertical > 0:
            return True

    def validate_move_right(self):
        if level_1_board[self.horizontal][self.vertical + 1] >= 2 and self.vertical < 9:
            return True

    def validate_move_up(self):
        if level_1_board[self.horizontal - 1][self.vertical] >= 2 and self.horizontal > 0:
            return True

    def validate_move_down(self):
        if level_1_board[self.horizontal + 1][self.vertical] >= 2 and self.horizontal < 9:
            return True

class PlayField(object):

    def __init__(self, level_layout):
        self.level_layout = level_layout

    def set_playfield(self):
        self.tile_objects = []
        self.enemy_objects = []
        self.boss_objects = []
        for y_coord in range(len(self.level_layout)):
            for x_coord in range(len(self.level_layout[y_coord])):
                self.get_tile_type(y_coord, x_coord)

    def get_tile_type(self, y_coord, x_coord):
        if self.level_layout[y_coord][x_coord] == 0:
            self.tile_objects.append(Wall(y_coord, x_coord))
        if self.level_layout[y_coord][x_coord] == 2:
            self.tile_objects.append(Floor(y_coord, x_coord))
        if self.level_layout[y_coord][x_coord] == 3:
            self.tile_objects.append(Floor(y_coord, x_coord))
            self.enemy_objects.append(TrashMob(y_coord, x_coord))
        if self.level_layout[y_coord][x_coord] == 5:
            self.tile_objects.append(Floor(y_coord, x_coord))
            self.boss_objects.append(Boss(y_coord, x_coord))

    # def print_playfield(self):
    #     self.print_tiles()
    #     self.print_enemies()
    #     self.print_bosses()
    #
    # def print_tiles(self):
    #     for tile in self.tile_objects:
    #         tile.draw()
    #
    # def print_enemies(self):
    #     for enemy in self.enemy_objects:
    #         enemy.draw()
    #
    # def print_bosses(self):
    #     for boss in self.boss_objects:
    #         boss.draw()

class Tile(object):

    def __init__(self, horizontal, vertical):
        self.size = 72
        self.horizontal = horizontal
        self.vertical = vertical

    def draw(self, pic):
        canvas.create_image(self.vertical * self.size, self.horizontal * self.size, image = pic, anchor = NW)

class Floor(Tile):

    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)
        self.floor = PhotoImage(file = 'assets/floor.png')

    def draw(self):
        super().draw(self.floor)

class Wall(Tile):

    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)
        self.wall = PhotoImage(file = 'assets/wall.png')

    def draw(self):
        super().draw(self.wall)

class Character(Tile):

    def __init__(self, vertical, horizontal):
        super().__init__(horizontal, vertical)

    def draw(self, hero_image):
        super().draw(hero_image)

class Hero(Character):

    def __init__(self, horizontal, vertical):
        self.hero_image = PhotoImage(file = 'assets/hero-down.png')
        super().__init__(horizontal, vertical)
        stats = Stats()
        Stats().__init__(hitpoint = 1, defense_point = 1, strike_point = 1, level = 1)
        Stats.set_hero_stats(self)
        Stats.get_stats(self)

    def draw(self):
        super().draw(self.hero_image)

    def hero_move_left(self, event):
        if Validator.validate_move_left(self):
            self.hero_image = PhotoImage(file = 'assets/hero-left.png')
            self.vertical -= 1
            super().draw(self.hero_image)
        else:
            self.hero_nomove()

    def hero_move_right(self, event):
        if Validator.validate_move_right(self):
            self.hero_image = PhotoImage(file = 'assets/hero-right.png')
            self.vertical += 1
            super().draw(self.hero_image)
        else:
            self.hero_nomove()

    def hero_move_up(self, event):
        if Validator.validate_move_up(self):
            self.hero_image = PhotoImage(file = 'assets/hero-up.png')
            self.horizontal -= 1
            super().draw(self.hero_image)
        else:
            self.hero_nomove()

    def hero_move_down(self, event):
        if Validator.validate_move_down(self):
            self.hero_image = PhotoImage(file = 'assets/hero-down.png')
            self.horizontal += 1
            super().draw(self.hero_image)
        else:
            self.hero_nomove()

    def hero_nomove(self):
        self.horizontal += 0
        self.vertical += 0

    def __str__(self):
        return "Hero: Level: {} HP: {} DP: {} SP: {} ".format(self.level, self.hitpoint, self.defense_point, self.strike_point)

class TrashMob(Tile):

    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)
        # Stats().__init__(hitpoint = 1, defense_point = 1, strike_point = 1, level = 1)
        # Stats.set_trashmob_stats(self)
        self.trashmob = PhotoImage(file = 'assets/skeleton.png')

    def draw(self):
        super().draw(self.trashmob)


class Boss(Tile):

    def __init__(self, horizontal, vertical):
        super().__init__(horizontal, vertical)
        # Stats().__init__(hitpoint = 1, defense_point = 1, strike_point = 1, level = 1)
        # Stats.set_boss_stats(self)
        self.boss = PhotoImage(file = 'assets/boss.png')

    def draw(self):
        super().draw(self.boss)



wanderer = PlayField(level_1_board)
wanderer.set_playfield()
# wanderer.print_playfield()
prrr = ScreenPrinter()
prrr.print_playfield()
majom = Hero(0, 0)
majom.draw()


main.bind('<Down>', majom.hero_move_down)
main.bind('<Up>', majom.hero_move_up)
main.bind('<Left>', majom.hero_move_left)
main.bind('<Right>', majom.hero_move_right)


canvas.pack()
main.mainloop()
